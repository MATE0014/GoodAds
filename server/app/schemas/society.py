# ...Pydantic Society schema...
from pydantic import BaseModel
from typing import List, Optional

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool
    
class ChoiceCreate(ChoiceBase):
    pass

class Choice(ChoiceBase):
    id: int
    question_id: int
    
    class Config:
        orm_mode = True  # For Pydantic v1, use from_attributes=True for v2
    
# Question schemas
class QuestionBase(BaseModel):
    question_text: str
    
class QuestionCreate(QuestionBase):
    choices: List[ChoiceCreate]
    
class Question(QuestionBase):
    id: int
    choices: List[Choice] = []
    
    class Config:
        orm_mode = True  # For Pydantic v1, use from_attributes=True for v2
    
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

    class Config:
        orm_mode = True  # For Pydantic v1, use from_attributes=True for v2
