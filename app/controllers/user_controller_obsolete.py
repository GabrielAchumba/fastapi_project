from fastapi import HTTPException
from app.dtos.user_dto import CreateUserDTO
from app.models.user_model import UserModel
from app.interfaces.user.user_controller_interface import IUserController
from app.services.user_service import IUserService
from typing import List, Optional

class UserController(IUserController):
    def __init__(self, user_service: IUserService):
        self.user_service = user_service

    async def create_user_controller(self, user_data: CreateUserDTO) -> UserModel:
        return await self.user_service.create_user(user_data)

    async def get_all_users_controller(self) -> List[UserModel]:
        return await self.user_service.get_users()

    async def get_user_controller(self, user_id: str) -> Optional[UserModel]:
        user = await self.user_service.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def update_user_controller(self, user_id: str, user_data: CreateUserDTO) -> Optional[UserModel]:
        updated_user = await self.user_service.update_user(user_id, user_data)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user

    async def delete_user_controller(self, user_id: str) -> dict:
        success = await self.user_service.delete_user(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}