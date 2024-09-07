from fastapi import Depends, HTTPException
from app.services.user_service import UserService, IUserService
from app.dtos.user_dto import CreateUserDTO
from app.models.user_model import UserModel
from app.interfaces.user.user_controller_interface import IUserController
from typing import List

# Inject the UserService using the IUserService interface
async def get_user_service() -> IUserService:
    return UserService()

# Inject the UserController with the UserService as dependency
async def get_user_controller(service: IUserService = Depends(get_user_service)):
    return UserController(service)

class UserController(IUserController):
    def __init__(self, user_service: IUserService):
        self.user_service = user_service

    async def create_user_controller(self, user_data: CreateUserDTO) -> UserModel:
        return await self.user_service.create_user(user_data)

    async def get_all_users_controller(self) -> List[UserModel]:
        return await self.user_service.get_users()

    async def get_user_controller(self, user_id: str) -> UserModel:
        user = await self.user_service.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def update_user_controller(self, user_id: str, user_data: CreateUserDTO) -> UserModel:
        updated_user = await self.user_service.update_user(user_id, user_data)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user

    async def delete_user_controller(self, user_id: str) -> dict:
        success = await self.user_service.delete_user(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}