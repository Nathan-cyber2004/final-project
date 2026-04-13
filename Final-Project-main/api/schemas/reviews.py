from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    order_id: int
    customer_id: int
    review_text: Optional[str] = None
    score: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    order_id: Optional[int] = None
    customer_id: Optional[int] = None
    review_text: Optional[str] = None
    score: Optional[int] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True