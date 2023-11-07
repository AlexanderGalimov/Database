from model.models import Auto, Manager
from service.service import AutoService, CustomerServiceManagerService

car1 = Auto(None, "BMW m5", True, 200, "../static/images/BMW%20m5.jpg")
car2 = Auto(None, "Lamborghini huracan", True, 500, "../static/images/Lamborghini huracan.jpg")
car3 = Auto(None, "WW polo", True, 75, "../static/images/WW polo.jpg")
car4 = Auto(None, "Ford mustang", True, 300, "../static/images/Ford mustang.jpg")
car5 = Auto(None, "Mclaren p1", True, 700, "../static/images/Mclaren p1.jpg")
car6 = Auto(None, "BMW m3", True, 240, "../static/images/BMW m3.jpg")
car7 = Auto(None, "Opel astra", True, 150, "../static/images/Opel astra.jpg")
car8 = Auto(None, "Volvo v40", True, 125, "../static/images/Volvo v40.jpg")

cs = AutoService()
cs.create(car1)
cs.create(car2)
cs.create(car3)
cs.create(car4)
cs.create(car5)
cs.create(car6)
cs.create(car7)
cs.create(car8)

manager1 = Manager("Anton Ivanov", 1)
manager2 = Manager("Vasya Petrov", 2)
manager3 = Manager("Ivan Ivanov", 1)

csms = CustomerServiceManagerService()
csms.create(manager1)
csms.create(manager2)
csms.create(manager3)
