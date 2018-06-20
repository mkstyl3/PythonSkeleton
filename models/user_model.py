from models.parent_model import ParentModel


class UserModel(ParentModel):
    def __init__(self):
        super(UserModel, self).__init__()

    def get(self, id):
        """ option 1 """
        return self.select("SELECT `name` FROM users WHERE `id` = :id;", {'id': id})
        """ option 2 """
        # result = self.call_proc('get_name', ["1"])
        return result
