from controllers.parent_controller import *

from models.user_model import UserModel


class UserController(ParentController):
    user = UserModel()

    def __init__(self):
        pass

    def get(self, params):
        return self.jsonParse(self.user.get(params['id']))

    def set(self, params):
        return self.jsonParse(self.user.get(params['id']))
