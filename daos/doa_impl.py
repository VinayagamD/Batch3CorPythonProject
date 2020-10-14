from daos import ProductDao, CategoryDao, SubCategoryDao


class ProductDaoImpl(ProductDao):
    """
    This class helps to do CRUD operation for the Product
    """

    def find_all(self):
        self.open_file(file=self.file_name, mode=self.read_mode)
        self.close_file()

    def find_by_id(self, id=0):
        super().find_by_id(id)

    def save(self, product):
        super().save(product)

    def update(self, product):
        super().update(product)

    def delete(self, product):
        super().delete(product)

    def delete_by_id(self, id):
        super().delete_by_id(id)


class CategoryDaoImpl(CategoryDao):
    """
    This class helps to do CRUD operations for the Category
    """

    def find_all(self):
        super().find_all()

    def find_by_id(self, id=0):
        super().find_by_id(id)

    def save(self, product):
        super().save(product)

    def update(self, product):
        super().update(product)

    def delete(self, product):
        super().delete(product)

    def delete_by_id(self, id):
        super().delete_by_id(id)


class SubCategoryDaoImpl(SubCategoryDao):
    """
    This class helps to do CRUD operations for the SubCategory
    """

    def find_all(self):
        super().find_all()

    def find_by_id(self, id=0):
        super().find_by_id(id)

    def save(self, product):
        super().save(product)

    def update(self, product):
        super().update(product)

    def delete(self, product):
        super().delete(product)

    def delete_by_id(self, id):
        super().delete_by_id(id)
