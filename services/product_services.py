from services import BaseService
from services import product_dao


class ProductService(BaseService):

    def __init__(self):
        self.dao = product_dao()

    def find_all(self):
        self.dao.find_all()

    def find_by_id(self, id=0):
        self.dao.find_by_id(id)

    def save(self, product):
        self.dao.save(product)

    def update(self, product):
        self.dao.update(product)

    def delete(self, product):
        self.dao.delete(product)

    def delete_by_id(self, id):
        self.dao.delete_by_id(id)
