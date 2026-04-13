from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
from .customers import Customer



class OrderBase(BaseModel):
    customer_id: int
    tracking_number: Optional[str] = None
    order_status: str = "pending"
    total_price: float


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    customer: Optional[Customer] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
