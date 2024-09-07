from abc import ABC, abstractmethod
from app.dtos.user_dto import CreateUserDTO
from app.models.user_model import UserModel
from typing import List, Optional

class IUserService(ABC):
    
    @abstractmethod
    async def create_user(self, user: CreateUserDTO) -> UserModel:
        pass

    @abstractmethod
    async def get_users(self) -> List[UserModel]:
        pass

    @abstractmethod
    async def get_user(self, user_id: str) -> Optional[UserModel]:
        pass

    @abstractmethod
    async def update_user(self, user_id: str, user_data: CreateUserDTO) -> Optional[UserModel]:
        pass

    @abstractmethod
    async def delete_user(self, user_id: str) -> bool:
        pass