import json


class ParentController:
    def __init__(self):
        pass

    def logger(self):
        return "logger"

    def jsonParse(self, object):
        try:
            return json.dumps(object)
        except Exception:
            return json.loads(object)
