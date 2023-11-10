from flask import Flask, render_template, request

from model.models import Client, Rent, CustomerServiceManager
from service.service import AutoService, ClientService, RentService, ManagerService, CustomerServiceManagerService
import time

car_service = AutoService()
client_service = ClientService()
rent_service = RentService()
manager_service = ManagerService()
customerServiceManagerService = CustomerServiceManagerService()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/car_choose')
def car_choose():
    cars = car_service.getAll()
    return render_template("car_choose.html", cars=cars)


@app.route('/rent/<int:idAuto>')
def rent(idAuto):
    return render_template("rent.html", idAuto=idAuto)


@app.route('/rent/', methods=['POST'])
def addRegistration():
    idAuto = request.form['autoId']
    fullName = request.form['fullName']
    contactInfo = request.form['contactInfo']
    amountOfDays = request.form['amountOfDays']

    if len(fullName) > 45 or len(fullName) == 0:
        return render_template("rent.html", idAuto=idAuto)
    if len(contactInfo) > 45 or len(fullName) == 0:
        return render_template("rent.html", idAuto=idAuto)
    try:
        idAuto = int(idAuto)
        amountOfDays = int(amountOfDays)
    except TypeError:
        print("error")
    except ValueError:
        print("error")

    client = Client(fullName, contactInfo)
    client_service.create(client)
    customerServiceManager = CustomerServiceManager(manager_service.get_random_manager(), client.idClient)
    customerServiceManagerService.create(customerServiceManager)
    auto = car_service.read(idAuto)

    curr_rent = Rent(client.idClient, amountOfDays, 0, True)
    rent_service.create(curr_rent)

    car_service.update(idAuto, curr_rent.idRent, auto.makeAndModel, False, auto.rentPrice, auto.imagePath)

    autos = car_service.getAll()
    print("--------------")
    for a in autos:
        d = a.serialize
        print(d)


    all_sum = rent_service.count_sum(curr_rent)
    print(f"all sum {all_sum}")
    rent_service.update(curr_rent.idRent, curr_rent.idClient, curr_rent.amountOfDays, all_sum, curr_rent.status)

    return render_template('confirm.html')


if __name__ == "__main__":
    app.run(port=4565, debug=False)
