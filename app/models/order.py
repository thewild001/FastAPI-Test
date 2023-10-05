from enum import Enum
from typing import List
from pydantic import BaseModel, Field, validator


class OrderStatus(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"


class OrderItem(BaseModel):
    id: int = Field(..., ge=1)
    item: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=1)
    price: float = Field(..., ge=0)
    status: OrderStatus


class OrderRequest(BaseModel):
    orders: List[OrderItem] = Field(..., min_items=1)
    criterion: str = Field(..., min_length=1)

    @validator("orders")
    def validate_orders(cls, orders):
        if not any(item.status == "completed" for item in orders):
            raise ValueError("At least one order item should have 'completed' status")
        return orders