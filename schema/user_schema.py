from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str] = None
    first_surname: str
    first_name: str
    other_name: Optional[str] = None
    country: str    
    email: Optional[str] = None

class UserUpdateSchema(BaseModel):
    first_surname: Optional[str] = None
    first_name: Optional[str] = None
    other_name: Optional[str] = None
    country: Optional[str] = None

