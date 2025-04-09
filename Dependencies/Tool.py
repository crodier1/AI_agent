from pydantic import BaseModel
from typing import Callable

class Tool(BaseModel):
    name: str
    description: str
    func: Callable