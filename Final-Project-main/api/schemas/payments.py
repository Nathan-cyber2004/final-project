from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    card_info: Optional[str] = None
    transaction_status: str = "pending"
    payment_type: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    card_info: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None


class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True