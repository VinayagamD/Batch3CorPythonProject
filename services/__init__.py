from .base_services import BaseService
from .product_services import ProductService
from daos import ProductDao


def product_dao():
    return ProductDao()
