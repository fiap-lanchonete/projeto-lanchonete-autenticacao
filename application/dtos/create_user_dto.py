from pydantic import BaseModel as PydanticBaseModel, EmailStr, Field

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class CreateUserDto(BaseModel):
  name: str
  cpf: str = Field(min_length=11, max_length=11)
  email: EmailStr
