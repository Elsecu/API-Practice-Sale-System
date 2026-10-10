from pydantic import BaseModel, Field, EmailStr, ConfigDict

#Products SCHEMAS
class ProductBase(BaseModel):
    product: str = Field(max_length=48)
    unit: int = Field(gt=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    product: str | None = Field(default=None, max_length=48)
    unit: int | None = Field(default=None, gt=0)

class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)