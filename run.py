from products import Product
from cart import ShoppingCart

car = ShoppingCart()
monit = Product('Monit', 1000)
beer = Product('Beer', 5)
rice = Product('Rice', 5)
banana = Product('Banana', 5)

car.add_procut(monit)
car.add_procut(beer)
car.add_procut(rice)
car.add_procut(banana)

car.finish_shopping()