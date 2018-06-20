from utils.db_connect import *


class ParentModel(object):
    def __init__(self):
        pass

    def insert(self):
        return "exec_insert"

    def update(self):
        return "exec_update"

    def delete(self):
        return "exec_delete"

    def select(self, query, params={}):
        result = connection.execute(text(query), params)
        # return [row for row in connection.fetchall()]
        return [dict(row) for row in result]

    def call_proc(self, procedure, params=[]):
        result = connection.callproc(procedure, params)
        return [row for row in list(connection.fetchall())]
