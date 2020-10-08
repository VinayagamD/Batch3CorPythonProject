from .product_controller import ProductController
from services import ProductServiceImpl


def product_service():
    return ProductServiceImpl()
