from pydantic import BaseModel

class User(BaseModel):
  name: str
  full_name: str | None = None
