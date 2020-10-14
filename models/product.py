class Product(object):
    """
    This class holds data communication for the product
    it should consists of following field id, name, category, subcategory, quantity, available
    """

    def __init__(self):
        self.id = 0
        self.name = ''
        self.category = ''
        self.subcategory = ''
        self.quantity = 0
        self.available = False


class Category:
    """
    This is model class to hold all categories
    it should contain following details id, name, subcategories
    """
    def __init__(self):
        self.id = 0
        self.name = ''
        self.sub_categories = []


class SubCategory:
    """
    This model class to hold all subcategory belonging to category
    it should contain following details id, name, category
    """

    def __init__(self):
        self.id = 0
        self.name = ''
        self.category: Category = None
