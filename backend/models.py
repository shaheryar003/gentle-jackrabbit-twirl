from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class MuseumTheme(BaseModel):
    id: str = Field(alias="_id")
    name: str
    description: str
    image: str

    class Config:
        populate_by_name = True

class MapPosition(BaseModel):
    top: str
    left: str

class MuseumObject(BaseModel):
    id: str = Field(alias="_id")
    title: str
    shortDescription: str
    contextualBackground: str
    galleryLocation: str
    image: str
    themeIds: List[str]
    mapPosition: MapPosition

    class Config:
        populate_by_name = True

class Tour(BaseModel):
    themeId: str
    size: str
    objectIds: List[str]

    class Config:
        populate_by_name = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str