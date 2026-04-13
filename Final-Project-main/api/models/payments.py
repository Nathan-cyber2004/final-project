from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    card_info = Column(String(100))  # Note: In production, never store full card info; use tokenized data
    transaction_status = Column(String(20), nullable=False, server_default="pending")
    payment_type = Column(String(20), nullable=False)  # e.g., credit_card, paypal

    order = relationship("Order", back_populates="payments")