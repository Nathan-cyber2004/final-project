from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    expiration_date = Column(DateTime, nullable=False)

    # Assuming promotions can be applied to orders; add relationships if needed
    # orders = relationship("Order", secondary="order_promotions")  # Many-to-many if applicable