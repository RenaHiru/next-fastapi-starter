from fastapi import FastAPI, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

# ==== C: Create 用のデータモデル ====
class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None

class Item(ItemCreate):
    id: int
    created_at: datetime

# ==== インメモリの簡易DB (ItemStoreクラス) ====
class ItemStore:
    def __init__(self):
        self.items: List[Item] = []
        self._next_id = 1
    
    def create_item(self, payload: ItemCreate) -> Item:
        nid = self._next_id
        self._next_id += 1
        now = datetime.utcnow()
        new_item = Item(id=nid, created_at=now, **payload.model_dump())
        self.items.append(new_item)
        return new_item

item_store = ItemStore()

# ==== Create API ====
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    return item_store.create_item(payload)