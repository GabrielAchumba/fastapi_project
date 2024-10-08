import motor.motor_asyncio
from bson import ObjectId
from app.models.user_model import UserModel
from app.dtos.user_dto import CreateUserDTO
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

# Initialize MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
users_collection = db['users']

async def create_user(user: CreateUserDTO):
    new_user = user.dict()
    result = await users_collection.insert_one(new_user)
    created_user = await users_collection.find_one({"_id": result.inserted_id})
    return UserModel(**created_user)

async def get_users():
    users = []
    async for user in users_collection.find():
        users.append(UserModel(**user))
    return users

async def get_user(user_id: str):
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return UserModel(**user)
    return None

async def update_user(user_id: str, user_data: CreateUserDTO):
    update_data = {k: v for k, v in user_data.dict().items() if v is not None}
    await users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    updated_user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if updated_user:
        return UserModel(**updated_user)
    return None

async def delete_user(user_id: str):
    result = await users_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0