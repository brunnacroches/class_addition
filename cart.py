from products import Product
from typing import Type

class ShoppingCart:
    
    def __init__(self) -> None:
        self.__products = []
    
    def add_procut(self, product:Type[Product]) -> None:
        self.__products.append(product)

    def finish_shopping(self) -> None:
        print('Finished shopping!')
        
        for product in self.__products:
            product.product_informations()