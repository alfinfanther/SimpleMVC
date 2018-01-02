from models import User,DBSession
from views import *

class Controller(object):
    def __init__(self):
        self.session = DBSession()

    def selUser(self):
        get_data = self.session.query(User).all()
        return showAllView(get_data)



if __name__ == '__main__':
    c = Controller()
    c.selUser()