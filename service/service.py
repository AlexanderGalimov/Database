from db.connection import Connection


class Service:
    def __init__(self):
        self.session = Connection()

    def create(self, fullName, departmentNumber):
        pass

    def read(self, manager_id):
        pass

    def update(self, manager_id, new_fullName, new_departmentNumber):
        pass

    def delete(self, manager_id):
        pass

    def  get_all(self):
        pass