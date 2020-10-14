class BaseDoa(object):
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


class DoaSourceUtil(BaseDoa):

    def __init__(self):
        self.file = None
        self.read_mode = "r"
        self.write_mode = "w"
        self.append_mode = "a"
        self.read_write_mode = "r+"

    def open_file(self, file, mode):
        self.file = open(file, mode)

    def close_file(self):
        if self.file is not None:
            self.file.close()


class ProductDao(DoaSourceUtil):

    def __init__(self):
        super().__init__()
        self.file_name = "../resources/product.json"


class CategoryDao(BaseDoa):

    def __init__(self):
        self.file_name = "category.json"


class SubCategoryDao(BaseDoa):
    def __init__(self):
        self.file_name = "sub_category.json"
