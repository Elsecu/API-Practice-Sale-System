from pydantic import BaseModel, Field, EmailStr, ConfigDict

class ClientBase(BaseModel):
    name: str = Field(min_length=2, max_length=48)
    email: str = Field(max_length=48, unique=True)
    edad: int = Field(gt=0, le=120)

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=48)
    email: str | None = Field(default=None, max_length=48, unique=True)
    edad: int | None = Field(default=None, gt=0, le=120)

class ClientResponse(ClientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)