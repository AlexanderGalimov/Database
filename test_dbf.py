from model.models import Manager, Client
from service.service import ManagerService, ClientService

m = Manager("muss", 116)
ma = ManagerService()

ma.create(m)

c = Client("juss", "pip")

ca = ClientService()
ca.create(c)