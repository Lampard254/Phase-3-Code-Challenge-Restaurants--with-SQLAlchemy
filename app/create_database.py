from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///./my_database.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Restaurant-Customer association table
restaurant_customer_association = Table(
    'restaurant_customer_association',
    Base.metadata,
    Column('restaurant_id', Integer, ForeignKey('restaurants.id')),
    Column('customer_id', Integer, ForeignKey('customers.id'))
)

# Restaurant class
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(200))
    rating = Column(Integer)

    customers = relationship('Customer', secondary=restaurant_customer_association, back_populates='restaurants')

# Customer class
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100))
    

    restaurants = relationship('Restaurant', secondary=restaurant_customer_association, back_populates='customers')

Base.metadata.create_all(bind=engine)

# Insert sample data
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Insert restaurants
restaurant1 = Restaurant(name="Restaurant A", description="Cozy ambiance", rating=4)
restaurant2 = Restaurant(name="Restaurant B", description="Great food variety", rating=5)
restaurant3 = Restaurant(name="Restaurant C", description="Family-friendly", rating=4.2)

session.add_all([restaurant1, restaurant2, restaurant3])
session.commit()

# Insert customers
customer1 = Customer(name="Alice", email="alice@email.com")
customer2 = Customer(name="Bob", email="bob@email.com")
customer3 = Customer(name="Charlie", email="charlie@email.com")

session.add_all([customer1, customer2, customer3])
session.commit()

# Adding relationships between restaurants and customers (sample associations)
restaurant1.customers.append(customer1)
restaurant1.customers.append(customer2)
restaurant2.customers.append(customer2)
restaurant2.customers.append(customer3)

session.commit()

print("Sample data inserted successfully.")
