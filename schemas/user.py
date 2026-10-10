from pydantic import BaseModel, Field, EmailStr, ConfigDict

#Users SCHEMAS
class UserBase(BaseModel):
    name: str = Field(min_length=2, max_length=48)
    email: EmailStr = Field(max_length=48, unique=True)
    age: int = Field(gt=0, le=120)

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=48)
    email: EmailStr | None = Field(default=None, max_length=48, unique=True)
    age: int | None = Field(default=None, gt=0, le=120)

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)