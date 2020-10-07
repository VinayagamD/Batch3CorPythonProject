from .product_controller import ProductController
from services import ProductService


def product_service():
    return ProductService()
