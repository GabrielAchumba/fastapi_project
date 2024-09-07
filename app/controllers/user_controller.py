from fastapi import HTTPException
from app.services.user_service import create_user, get_users, get_user, update_user, delete_user
from app.dtos.user_dto import CreateUserDTO

async def create_user_controller(user_data: CreateUserDTO):
    return await create_user(user_data)

async def get_all_users_controller():
    return await get_users()

async def get_user_controller(user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def update_user_controller(user_id: str, user_data: CreateUserDTO):
    updated_user = await update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

async def delete_user_controller(user_id: str):
    success = await delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}