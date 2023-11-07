import random
from abc import ABC, abstractmethod

from sqlalchemy.orm.exc import UnmappedInstanceError

from db.dbconnection import dbConnection
from model.models import Manager, Client, Disturbance, CustomerServiceManager, Rent, Auto


class Service(ABC):
    def __init__(self):
        self.connection = dbConnection()

    def create(self, *args) -> bool:
        pass

    @abstractmethod
    def read(self, *args):
        pass

    @abstractmethod
    def update(self, *args) -> bool:
        pass

    @abstractmethod
    def remove(self, *args) -> bool:
        pass

    @abstractmethod
    def getAll(self):
        pass


class ManagerService(Service):
    def __init__(self):
        super().__init__()

    def create(self, manager):
        try:
            self.connection.session.add(manager)
            self.connection.session.commit()
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def read(self, managerId):
        try:
            manager = self.connection.session.query(Manager).filter_by(idManager=managerId).first()
            return manager
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, managerId, newFullName, newDepartmentNumber):
        try:
            manager = self.read(managerId)
            manager.fullName = newFullName
            manager.departmentNumber = newDepartmentNumber
            self.connection.session.commit()
        except AttributeError as e:
            raise Exception(f"Error: {str(e)}")

    def remove(self, managerId):
        try:
            managerToRemove = self.read(managerId)
            self.connection.session.delete(managerToRemove)
            self.connection.session.commit()
        except UnmappedInstanceError as e:
            raise Exception(f"Error: {str(e)}")

    def get_random_manager(self):
        managers = self.connection.session.query(Manager.idManager).all()
        column_list = [item[0] for item in managers]
        if managers:
            return random.choice(column_list)
        else:
            return 0

    def getAll(self):
        return self.connection.session.query(Manager).all()


class ClientService(Service):
    def __init__(self):
        super().__init__()

    def create(self, client):
        try:
            self.connection.session.add(client)
            self.connection.session.commit()
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def read(self, clientId):
        try:
            client = self.connection.session.query(Client).filter_by(idClient=clientId).first()
            return client
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, clientId, newFullName, contactInfo):
        try:
            client = self.read(clientId)
            client.fullName = newFullName
            client.contactInfo = contactInfo
            self.connection.session.commit()
        except AttributeError as e:
            raise Exception(f"Error: {str(e)}")

    def remove(self, clientId):
        try:
            clientToRemove = self.read(clientId)
            self.connection.session.delete(clientToRemove)
            self.connection.session.commit()
        except UnmappedInstanceError as e:
            raise Exception(f"Error: {str(e)}")

    def getAll(self):
        return self.connection.session.query(Client).all()


class DisturbanceService(Service):

    def __init__(self):
        super().__init__()

    def create(self, disturbance):
        try:
            self.connection.session.add(disturbance)
            self.connection.session.commit()
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def read(self, disturbanceId):
        try:
            disturbance = self.connection.session.query(Disturbance).filter_by(idDisturbance=disturbanceId).first()
            return disturbance
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, disturbanceId, newClient, description):
        try:
            disturbance = self.read(disturbanceId)
            disturbance.idClient = newClient
            disturbance.description = description
            self.connection.session.commit()
        except AttributeError as e:
            raise Exception(f"Error: {str(e)}")

    def remove(self, disturbanceId):
        try:
            disturbanceToRemove = self.read(disturbanceId)
            self.connection.session.delete(disturbanceToRemove)
            self.connection.session.commit()
        except UnmappedInstanceError as e:
            raise Exception(f"Error: {str(e)}")

    def getAll(self):
        return self.connection.session.query(Disturbance).all()


class CustomerServiceManagerService(Service):

    def __init__(self):
        super().__init__()

    def create(self, customerServiceManager):
        try:
            self.connection.session.add(customerServiceManager)
            self.connection.session.commit()
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def read(self, managerId, clientId):
        try:
            customerServiceManager = self.connection.session.query(CustomerServiceManager).filter_by(
                idManager=managerId,
                idClient=clientId).first()
            return customerServiceManager
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, managerId, clientId, newManagerId, newClientId):
        try:
            customerServiceManager = self.read(managerId, clientId)
            manager = self.connection.session.query(Manager).filter_by(idManager=newManagerId).first()
            client = self.connection.session.query(Client).filter_by(idClient=newClientId).first()
            if manager is not None and client is not None:
                customerServiceManager.idManager = newManagerId
                customerServiceManager.idClient = newClientId
                self.connection.session.commit()
        except AttributeError as e:
            raise Exception(f"Error: {str(e)}")

    def remove(self, managerId, clientId):
        try:
            csmToRemove = self.read(managerId, clientId)
            self.connection.session.delete(csmToRemove)
            self.connection.session.commit()
        except UnmappedInstanceError as e:
            raise Exception(f"Error: {str(e)}")

    def getAll(self):
        return self.connection.session.query(CustomerServiceManager).all()


class RentService(Service):

    def __init__(self):
        super().__init__()

    def create(self, rent):
        try:
            self.connection.session.add(rent)
            self.connection.session.commit()
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def read(self, rentId):
        try:
            disturbance = self.connection.session.query(Rent).filter_by(idRent=rentId).first()
            return disturbance
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, rentId, clientId, amountOfDays, newSum, status):
        try:
            rent = self.read(rentId)
            rent.idClient = clientId
            rent.amountOfDays = amountOfDays
            if newSum == 0 or newSum is None:
                rent.sum = self.count_sum(rentId)
            else:
                rent.sum = newSum
            rent.status = status
            self.connection.session.commit()
        except AttributeError as e:
            raise Exception(f"Error: {str(e)}")

    def remove(self, rentId):
        try:
            rentToRemove = self.read(rentId)
            self.connection.session.delete(rentToRemove)
            self.connection.session.commit()
        except UnmappedInstanceError as e:
            raise Exception(f"Error: {str(e)}")

    def getAll(self):
        return self.connection.session.query(Rent).all()

    def count_sum(self, rentId):
        try:
            autos_for_rent = self.connection.session.query(Auto).filter(Auto.idRent == rentId).all()
            total_rent = 0
            for auto in autos_for_rent:
                total_rent += auto.rentPrice * auto.rent.amountOfDays
            return total_rent
        except AttributeError as e:
            raise Exception(f"Error: {str(e)}")


class AutoService(Service):
    def __init__(self):
        super().__init__()

    def create(self, auto):
        try:
            self.connection.session.add(auto)
            self.connection.session.commit()
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def read(self, autoId):
        try:
            auto = self.connection.session.query(Auto).filter_by(idAuto=autoId).first()
            return auto
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def update(self, autoId, rentId, newMakeAndModel, status, rentPrice, path):
        try:
            auto = self.read(rentId)
            auto.idRent = rentId
            auto.makeAndModel = newMakeAndModel
            auto.status = status
            auto.rentPrice = rentPrice
            auto.imagePath = path
            self.connection.session.commit()
        except AttributeError as e:
            raise Exception(f"Error: {str(e)}")

    def remove(self, autoId):
        try:
            autoToRemove = self.read(autoId)
            self.connection.session.delete(autoToRemove)
            self.connection.session.commit()
        except UnmappedInstanceError as e:
            raise Exception(f"Error: {str(e)}")

    def getAll(self):
        return self.connection.session.query(Auto).all()
