from services import product_dao


class BaseService(object):
    """
    This class has base rules for the DAO
    """

    def find_all(self):
        pass

    def find_by_id(self, id=0):
        pass

    def save(self, product):
        pass

    def update(self, product):
        pass

    def delete(self, product):
        pass

    def delete_by_id(self, id):
        pass


class ProductService(BaseService):

    def __init__(self):
        self.dao = product_dao()
