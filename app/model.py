from pydantic import BaseModel, Field, EmailStr


#User schema
class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Aiman dev Task assessment",
                "email": "Aimankhanji123@gmail.com",
                "password": "password123"
            }
        }


