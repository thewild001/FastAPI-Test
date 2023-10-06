from enum import Enum
from typing import List
from pydantic import BaseModel, Field, validator


class OrderStatus(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"


class OrderItem(BaseModel):
    id: int = Field(..., ge=1, description="The ID must be a positive integer")
    item: str = Field(..., min_length=1, description="The item name cannot be empty")
    quantity: int = Field(..., ge=1, description="The quantity must be a positive integer")
    price: float = Field(..., ge=0, description="The price cannot be negative")
    status: OrderStatus


class OrderRequest(BaseModel):
    orders: List[OrderItem] = Field(..., min_items=1, description="Must provide at least one order")
    criterion: str = Field(..., min_length=1)

    @validator("orders")
    def validate_orders(cls, orders):
        if not any(item.status == "completed" for item in orders):
            raise ValueError("At least one order item should have 'completed' status")
        return orders