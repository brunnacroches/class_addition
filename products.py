class Product:
    def __init__(self, product_name: str, product_value: int) -> None:
        self.__product_name = product_name
        self.__product_value = product_value
    
    def product_informations(self) -> None:
        print('Product: {} / value: USD {},00'.format(self.__product_name, self.__product_value))
    
