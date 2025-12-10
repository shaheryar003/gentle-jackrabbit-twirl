import os
from typing import List
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from models import UserCreate, UserResponse, UserLogin, Token, MuseumTheme, MuseumObject
from security import get_password_hash, verify_password, create_access_token, get_current_user
from database import db

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to MongoDB
    db.connect()
    yield
    # Shutdown: Close connection
    db.close()

app = FastAPI(title="Museum Thematic Tour Backend", lifespan=lifespan)

# Configure CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "*" # Allow all for development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
async def health_check():
    """
    Checks the database connection and returns status.
    """
    if not db.client:
        raise HTTPException(status_code=500, detail="Database client not initialized")
    
    try:
        # Perform a real operation to check connection
        await db.client.admin.command('ping')
        return {"status": "ok", "message": "Database connected successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

@app.post("/api/v1/auth/signup", response_model=UserResponse, status_code=201)
async def signup(user: UserCreate):
    database = db.get_db()
    if database is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    
    # Check if user already exists
    if await database.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    user_dict = {
        "email": user.email,
        "password_hash": get_password_hash(user.password)
    }
    
    result = await database.users.insert_one(user_dict)
    
    return UserResponse(id=str(result.inserted_id), email=user.email)

@app.post("/api/v1/auth/login", response_model=Token)
async def login(user_login: UserLogin):
    database = db.get_db()
    if database is None:
        raise HTTPException(status_code=500, detail="Database not initialized")

    user = await database.users.find_one({"email": user_login.email})
    if not user or not verify_password(user_login.password, user["password_hash"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        subject=user["email"]
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/v1/users/me", response_model=UserResponse)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return UserResponse(id=str(current_user["_id"]), email=current_user["email"])

@app.get("/api/v1/themes", response_model=List[MuseumTheme], response_model_by_alias=False)
async def get_themes():
    database = db.get_db()
    if database is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    
    themes = await database.themes.find().to_list(length=100)
    return themes

@app.get("/api/v1/themes/{theme_id}", response_model=MuseumTheme, response_model_by_alias=False)
async def get_theme(theme_id: str):
    database = db.get_db()
    if database is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    
    theme = await database.themes.find_one({"_id": theme_id})
    if theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    return theme

@app.get("/api/v1/objects/{object_id}", response_model=MuseumObject, response_model_by_alias=False)
async def get_object(object_id: str):
    database = db.get_db()
    if database is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    
    obj = await database.objects.find_one({"_id": object_id})
    if obj is None:
        raise HTTPException(status_code=404, detail="Object not found")
    
    return obj

@app.get("/api/v1/tours/{theme_id}/{size}", response_model=List[MuseumObject], response_model_by_alias=False)
async def get_tour_objects(theme_id: str, size: str):
    database = db.get_db()
    if database is None:
        raise HTTPException(status_code=500, detail="Database not initialized")
    
    # 1. Find the tour configuration
    # Note: Case-sensitive match for size (e.g., "Small")
    tour = await database.tours.find_one({"themeId": theme_id, "size": size})
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour configuration not found")
    
    object_ids = tour.get("objectIds", [])
    if not object_ids:
        return []

    # 2. Fetch the actual objects
    # Note: Mongo's $in doesn't guarantee order, so we'll fetch all and re-order in Python
    cursor = database.objects.find({"_id": {"$in": object_ids}})
    objects_list = await cursor.to_list(length=len(object_ids))
    
    # 3. Create a mapping for quick lookup
    objects_map = {obj["_id"]: obj for obj in objects_list}
    
    # 4. Reconstruct the list in the correct order
    ordered_objects = []
    for oid in object_ids:
        if oid in objects_map:
            ordered_objects.append(objects_map[oid])
            
    return ordered_objects

@app.get("/")
async def root():
    return {"message": "Welcome to the Museum Thematic Tour API"}