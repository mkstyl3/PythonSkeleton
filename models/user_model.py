from models.parent_model import ParentModel


class UserModel(ParentModel):
    __tablename__ = 'users'

    def __init__(self):
        super(UserModel, self).__init__()

    def get(self, id):
        """ option 1 """
        return self.execute("SELECT * FROM users WHERE `id` = :id;", {'id': id})
        """ option 2 """
        # return self.call_proc('get_name', [id])
        """ option 3 """
        # return self.select("users.id={id}".format(id=id))

    def set(self, id, name, surnames):
        """ option 1"""
        return self.update('id=%s' % (id), [('name', name), ('surnames', surnames)])
        """ option 2 """
        # return self.call_proc('set_user', [id, name, surnames])
