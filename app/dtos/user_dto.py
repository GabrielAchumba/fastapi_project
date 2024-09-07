from pydantic import BaseModel

class CreateUserDTO(BaseModel):
    name: str
    email: str
    age: int

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "age": 30
            }
        }