from fastapi import APIRouter
from app.dtos.user_dto import CreateUserDTO
from app.controllers.user_controller_obsolete import (
    create_user_controller,
    get_all_users_controller,
    get_user_controller,
    update_user_controller,
    delete_user_controller
)

router = APIRouter()

@router.post("/users")
async def create_user(user_data: CreateUserDTO):
    return await create_user_controller(user_data)

@router.get("/users")
async def get_users():
    return await get_all_users_controller()

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    return await get_user_controller(user_id)

@router.put("/users/{user_id}")
async def update_user(user_id: str, user_data: CreateUserDTO):
    return await update_user_controller(user_id, user_data)

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    return await delete_user_controller(user_id)