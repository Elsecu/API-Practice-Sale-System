from sqlalchemy import Column,  Integer, String
from database import Base
#Tabla de usuarios
class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    age = Column(Integer, nullable=False)
#Tabla de productos
class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, nullable=False)
    unit = Column(Integer, nullable=False)
#Tabla de clientes
class ClientModel(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True, unique=True)
    edad = Column(Integer, nullable=False)
