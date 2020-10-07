class Cart:
    """
    This class maintains all the cart product
    it should consists of cart id , date and list of product
    """

    def __init__(self):
        self.id = 0
        self.date = None
        self.products = []


class Shipped:
    """
    This class maintains all the information of shipped product
    it should consists of id, shipping address, status, order date and users
    """

    def __init__(self):
        self.id = 0
        self.address = ""
        self.order_date = ''
        self.status = ''
        self.products = []