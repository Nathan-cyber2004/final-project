from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    review_text = Column(String(500))
    score = Column(Integer, nullable=False)  # e.g., 1-5 rating

    order = relationship("Order", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")