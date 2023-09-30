import mysql.connector
from random import randint
from faker import Faker

db_connection = mysql.connector.connect(
    user='root', password='185206',
    host='127.0.0.1', database='mydb',
    auth_plugin='mysql_native_password'
)

cursor = db_connection.cursor()

fcker = Faker()
for _ in range(1000):
    name = f"{fcker.name()}"
    print(name)

    # SQL-запрос для вставки данных
    insert_query = f"INSERT INTO Client (fullName) VALUES ('{name}')"

    cursor.execute(insert_query)

db_connection.commit()

cursor.close()
db_connection.close()