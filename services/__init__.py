from .base_services import BaseService, ProductService
from daos import ProductDao, CategoryDao, SubCategoryDao, ProductDaoImpl, CategoryDaoImpl, SubCategoryDaoImpl
from .impl_services import ProductServiceImpl


def product_dao():
    return ProductDaoImpl()
