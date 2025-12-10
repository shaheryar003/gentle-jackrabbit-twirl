import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    print("Error: MONGODB_URI not found in environment variables.")
    exit(1)

async def verify():
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client["museum_tour"]

    try:
        print("--- Verification Start ---")
        
        # Verify Themes
        theme_count = await db.themes.count_documents({})
        print(f"Themes Count: {theme_count}")
        first_theme = await db.themes.find_one()
        print(f"Sample Theme: {first_theme}\n")

        # Verify Objects
        object_count = await db.objects.count_documents({})
        print(f"Objects Count: {object_count}")
        first_object = await db.objects.find_one()
        print(f"Sample Object: {first_object}\n")

        # Verify Tours
        tour_count = await db.tours.count_documents({})
        print(f"Tours Count: {tour_count}")
        first_tour = await db.tours.find_one()
        print(f"Sample Tour: {first_tour}\n")
        
        print("--- Verification End ---")

    except Exception as e:
        print(f"An error occurred during verification: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(verify())