from abc import ABC

import faker
from faker import Faker


class Generator(ABC):
    def __init__(self):
        self.faker = Faker()

    def generateClient(self):
        for _ in range(1000):
            name = f"{faker.name()}"
            print(name)

            # SQL-запрос для вставки данных
            insert_query = f"INSERT INTO Client (fullName) VALUES ('{name}')"