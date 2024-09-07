from fastapi import APIRouter, Depends
from app.controllers.user_controller import UserController, get_user_controller
from app.dtos.user_dto import CreateUserDTO

# Create an APIRouter instance
router = APIRouter()


@router.post("/users")
async def create_user(user_data: CreateUserDTO, controller: UserController = Depends(get_user_controller)):
    return await controller.create_user_controller(user_data)


@router.get("/users")
async def get_all_users(controller: UserController = Depends(get_user_controller)):
    print("seen")
    return await controller.get_all_users_controller()


@router.get("/users/{user_id}")
async def get_user(user_id: str, controller: UserController = Depends(get_user_controller)):
    return await controller.get_user_controller(user_id)


@router.put("/users/{user_id}")
async def update_user(user_id: str, user_data: CreateUserDTO, controller: UserController = Depends(get_user_controller)):
    return await controller.update_user_controller(user_id, user_data)


@router.delete("/users/{user_id}")
async def delete_user(user_id: str, controller: UserController = Depends(get_user_controller)):
    return await controller.delete_user_controller(user_id)
