from pydantic import BaseModel, Field, EmailStr

#POST schema
class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Post add only with JWT.",
                "content": "We'll be using PyJWT to perform Task assessment"
            }
        }


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


