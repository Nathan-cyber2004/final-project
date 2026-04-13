from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(String(50), unique=True)
    order_status = Column(String(20), nullable=False, server_default="pending")
    total_price = Column(DECIMAL(10, 2), nullable=False, server_default='0.00')

    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populates="order")
    reviews = relationship("Review", back_populates="order")