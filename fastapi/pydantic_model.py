from typing import List, Optional
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., description="name of item")
    id: int = Field(..., description="id")
    desc: Optional[str] = Field(None, description="desc")  # Optional should default to None

# Correct type for `id` is int
item = Item(name="Widget", id=19)
print(item.dict())
