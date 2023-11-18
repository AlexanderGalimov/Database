from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db.dbconnection import DbConnection

Base = declarative_base()
connection = DbConnection()


class Manager(Base):
    __tablename__ = 'Manager'

    idManager = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(45), nullable=False)
    departmentNumber = Column(Integer, nullable=False)

    def __init__(self, fullName, departmentNumber):
        self.fullName = fullName
        self.departmentNumber = departmentNumber

    @property
    def serialize(self):
        return {
            "idManager": self.idManager,
            "fullName": self.fullName,
            "departmentNumber": self.departmentNumber
        }


class Client(Base):
    __tablename__ = 'Client'

    idClient = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(45), nullable=False)
    contactInfo = Column(String(45))

    def __init__(self, fullName, contactInfo):
        self.fullName = fullName
        self.contactInfo = contactInfo

    @property
    def serialize(self):
        return {
            "idClient": self.idClient,
            "fullName": self.fullName,
            "contactInfo": self.contactInfo
        }


class Disturbance(Base):
    __tablename__ = 'Disturbance'

    idDisturbance = Column(Integer, primary_key=True)
    idClient = Column(Integer, ForeignKey('Client.idClient'), nullable=False)
    client = relationship("Client")
    description = Column(String(100), nullable=False)

    def __init__(self, idClient, description):
        self.idClient = idClient
        self.description = description

    @property
    def serialize(self):
        return {
            "idDisturbance": self.idDisturbance,
            "idClient": self.idClient,
            "client": self.client,
            "description": self.description
        }


class CustomerServiceManager(Base):
    __tablename__ = 'Customer Service Manager'

    idManager = Column(Integer, ForeignKey('Manager.idManager'), primary_key=True)
    idClient = Column(Integer, ForeignKey('Client.idClient'), primary_key=True)
    manager = relationship("Manager")
    client = relationship("Client")

    def __init__(self, idManager, idClient):
        self.idManager = idManager
        self.idClient = idClient

    @property
    def serialize(self):
        return {
            "idManager": self.idManager,
            "idClient": self.idClient,
            "manager": self.manager,
            "client": self.client
        }


class Rent(Base):
    __tablename__ = 'Rent'

    idRent = Column(Integer, primary_key=True, autoincrement=True)
    idClient = Column(Integer, ForeignKey('Client.idClient'), nullable=False)
    amountOfDays = Column(Integer, nullable=False)
    sum = Column(Float)
    status = Column(Integer, nullable=False)

    def __init__(self, idClient, amountOfDays, s, status):
        self.idClient = idClient
        self.amountOfDays = amountOfDays
        self.sum = s
        self.status = status

    @property
    def serialize(self):
        return {
            "idRent": self.idRent,
            "idClient": self.idClient,
            "amountOfDays": self.amountOfDays,
            "sum": self.sum,
            "status": self.status
        }


class Auto(Base):
    __tablename__ = 'Auto'

    idAuto = Column(Integer, primary_key=True, autoincrement=True)
    idRent = Column(Integer, ForeignKey('Rent.idRent'), nullable=True)  #
    brand = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    status = Column(Integer, nullable=False)
    rentPrice = Column(Float, nullable=False)
    imagePath = Column(String(45), nullable=True)

    def __init__(self, idRent, brand, model, status, rentPrice, imagePath):
        self.idRent = idRent
        self.brand = brand
        self.model = model
        self.status = status
        self.rentPrice = rentPrice
        self.imagePath = imagePath

    @property
    def serialize(self):
        return {
            "idAuto": self.idAuto,
            "idRent": self.idRent,
            "brand": self.brand,
            "model": self.model,
            "status": self.status,
            "rentPrice": self.rentPrice,
            "imagePath": self.imagePath
        }
