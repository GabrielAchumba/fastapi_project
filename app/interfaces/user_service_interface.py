from typing import List, Optional
from app.models.user_model import UserModel

class UserServiceInterface:
    def get_user_by_id(self, user_id: int) -> Optional[UserModel]:
        raise NotImplementedError
    
    def create_user(self, user: User) -> User:
        raise NotImplementedError