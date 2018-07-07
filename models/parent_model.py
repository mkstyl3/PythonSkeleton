from utils.db_connect import *


class ParentModel(object):
    __tablename__ = "test"
    __table__ = None
    
    def __init__(self):
        self.__table__ = Table(self.__tablename__, MetaData(), autoload=True, autoload_with=engine)
    
    def getColumns(self):
        return self.__table__.columns.keys()
    
    def delete(self):
        return "exec_delete"

    def insert(self):
        return "exec_insert"

    def update(self, where, sets={}):
        query = update(self.__table__)\
                .where(text(where)) \
                .values(sets)
        result = connection.execute(query)
        connection.commit()
        connection.close()
        return result.rowcount

    def select(self, where=None, columns=None):
        """ select columns """
        if columns is not None:
            cols = [text(col) for col in columns]
        else:
            cols = [self.__table__.c[col] for col in self.getColumns()]
        """ select table """
        query = select(cols)
        # query = query.select_from(self.__table__)
        query = query.select_from(self.__table__.join(text("rols"), text("users.id=rols.id")))
        """ select where """
        if where is not None:
            query = query.where(text(where))
        """ execute query """
        result = connection.execute(query)
        return [dict(row) for row in result]
    
    def execute(self, query, bind_params={}):
        result = connection.execute(text(query), bind_params)
        return [dict(row) for row in result]
    
    def call_proc(self, procedure, bind_params=[]):
        cursor.callproc(procedure, bind_params)
        raw_connection.commit()
        return list(cursor.fetchall())
