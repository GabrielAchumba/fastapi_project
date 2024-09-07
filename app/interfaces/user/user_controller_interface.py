from abc import ABC, abstractmethod
from app.dtos.user_dto import CreateUserDTO
from app.models.user_model import UserModel
from typing import List, Optional

class IUserController(ABC):
    
    @abstractmethod
    async def create_user_controller(self, user_data: CreateUserDTO) -> UserModel:
        pass

    @abstractmethod
    async def get_all_users_controller(self) -> List[UserModel]:
        pass

    @abstractmethod
    async def get_user_controller(self, user_id: str) -> Optional[UserModel]:
        pass

    @abstractmethod
    async def update_user_controller(self, user_id: str, user_data: CreateUserDTO) -> Optional[UserModel]:
        pass

    @abstractmethod
    async def delete_user_controller(self, user_id: str) -> dict:
        pass