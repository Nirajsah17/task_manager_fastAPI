from pydantic import BaseModel
from typing import Optional


class TaskSchema(BaseModel):
  title: str
  description: str
  is_completed: bool = False


class TaskResponseSchema(BaseModel):
  id: int
  title: str
  description: str
  is_completed: bool
  user_id:Optional[int] = 0