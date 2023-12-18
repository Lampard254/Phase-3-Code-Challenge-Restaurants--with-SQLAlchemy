from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='restaurant_customer_association', back_populates='customers')

    # Define your methods here (e.g., full_name(), favorite_restaurant(), etc.)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Other methods as described in the assignment

    # ...

