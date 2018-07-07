import sqlalchemy

from pymysql import *
from config.database import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


# sqlalchemy.__version__

class DB(object):
    __tablename__ = "test"
    __table__ = None
    engine = None
    Session = None
    connection = None
    raw_connection = None
    cursor = None

    def __init__(self):
        try:
            connection = None
            str_connect = "mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}?charset=utf8"
            self.engine = sqlalchemy.create_engine(
                str_connect.format(
                    db_user=DB_USER,
                    db_pass=DB_PASS,
                    db_host=DB_HOST,
                    db_name=DB_NAME
                ), echo=True)
            self.Session = sessionmaker(bind=self.engine)
            self.connection = self.Session(bind=self.engine.connect())
            self.raw_connection = self.engine.raw_connection()
            self.cursor = self.raw_connection.cursor(cursors.DictCursor)
            self.__table__ = Table(self.__tablename__, MetaData(), autoload=True, autoload_with=self.engine)
            print("sqlalchemy version: " + sqlalchemy.__version__)
        except Exception:
            raise Exception('No connection to database')

    def getColumns(self):
        return self.__table__.columns.keys()

    def delete(self):
        return "exec_delete"

    def insert(self):
        return "exec_insert"

    def update(self, where, sets=[()]):
        query = update(self.__table__) \
            .where(text(where)) \
            .values(sets)
        result = self.connection.execute(query)
        self.connection.commit()
        self.connection.close()
        return result.rowcount

    def select(self, where=None, columns=None):
        self.connection.commit()  # clear old data
        """ select columns """
        if columns is not None:
            cols = [text(col) for col in columns]
        else:
            cols = [self.__table__.c[col] for col in self.getColumns()]
        """ select table """
        query = select(cols)
        query = query.select_from(self.__table__)
        # query = query.select_from(self.__table__.join(text("rols"), text("users.id=rols.id")))
        """ select where """
        if where is not None:
            query = query.where(text(where))
        """ execute query """
        result = self.connection.execute(query)
        self.engine.dispose()
        return [dict(row) for row in result]

    def execute(self, query, bind_params={}):
        self.connection.commit()  # clear old data
        result = self.connection.execute(text(query), bind_params)
        self.engine.dispose()
        return [dict(row) for row in result]

    def call_proc(self, procedure, bind_params=[]):
        self.cursor.callproc(procedure, bind_params)
        result = list(self.cursor.fetchall())
        self.raw_connection.commit()
        self.engine.dispose()
        return result
