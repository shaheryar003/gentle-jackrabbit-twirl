import os
from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load .env from the same directory as this file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = "museum_tour" # Default name, or extract from URI if needed, but keeping it simple for now or relying on default db

class Database:
    client: AsyncIOMotorClient = None

    def connect(self):
        if MONGODB_URI:
            self.client = AsyncIOMotorClient(MONGODB_URI)
            print("Connected to MongoDB client")
        else:
            print("MONGODB_URI not set")

    def close(self):
        if self.client:
            self.client.close()
            print("Closed MongoDB connection")

    def get_db(self):
        if self.client:
             return self.client[DB_NAME]
        return None

db = Database()

async def get_database():
    return db.get_db()