from pydantic import BaseModel as PydanticBaseModel, EmailStr, Field

class BaseModel(PydanticBaseModel):
    """Base model for data transfer objects."""
    class Config:
        """Pydantic configuration."""
        arbitrary_types_allowed = True

class CreateUserDto(BaseModel):
    """Data transfer object for creating a new user."""
    name: str
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr
