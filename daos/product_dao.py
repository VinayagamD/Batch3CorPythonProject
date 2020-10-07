from daos import BaseDoa


class ProductDao(BaseDoa):
    """
    This class helps to do CRUD operation for the Product
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


class CategoryDao(BaseDoa):
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


class SubCategoryDao(BaseDoa):
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
