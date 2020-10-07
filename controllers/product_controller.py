from controllers import product_service


class ProductController:
    """
    This product controller python class
    """

    def __init__(self):
        self.service = product_service()
