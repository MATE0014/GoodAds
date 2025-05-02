# ...Pydantic Society schema...
from pydantic import BaseModel
from typing import Optional
  
# Society schemas
class SocietyBase(BaseModel):
    name: str
    description: Optional[str] = None
    logo_url: Optional[str] = None
    website_url: Optional[str] = None  # Added to match the model

class SocietyCreate(SocietyBase):
    pass

class SocietyUpdate(SocietyBase):
    name: Optional[str] = None  # Make fields optional for PATCH updates
    
class Society(SocietyBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # For Pydantic v1, use from_attributes=True for v2
