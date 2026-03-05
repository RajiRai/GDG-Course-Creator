from pydantic import BaseModel, Field
from typing import List

class ResearchOutput(BaseModel):
    topic: str
    key_facts: List[str]
    sources: List[str]
    confidence_score: float

class CourseModule(BaseModel):
    title: str
    lessons: List[str]
    learning_outcome: str

class CourseOutline(BaseModel):
    title: str
    description: str
    modules: List[CourseModule]
