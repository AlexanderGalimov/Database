from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class dbConnection:
    def __init__(self):
        self.session = None
        self.engine = None
        self._instance = None
        self.create_connection()

    def create_connection(self):
        self.engine = create_engine('mysql://root:185206@localhost/mydb', echo=True)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def close_connection(self):
        self.session.close()
