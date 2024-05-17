from copy import deepcopy


class OrderPrototype:
    def __init__(self):
        self.order_number = 0
        self.products = []
        self.total_price = 0.0

  
    def clone(self):
        return deepcopy(self)


class Order:
    def __init__(self, prototype: OrderPrototype):
        self.order_number = prototype.order_number
        self.products = prototype.products[:]
        self.total_price = prototype.total_price

  
    def __str__(self):
        return f"Order Number: {self.order_number}\nProducts: {', '.join(self.products)}\nTotal Price: {self.total_price}"


prototype_order = OrderPrototype()
prototype_order.order_number = 1001
prototype_order.products = ["Product A", "Product B", "Product C"]
prototype_order.total_price = 150.00

# Создаем новый заказ на основе прототипа
order1 = Order(prototype_order.clone())
order1.order_number = 1002
order1.total_price = 200.00

# Создаем еще один новый заказ на основе прототипа
order2 = Order(prototype_order.clone())
order2.order_number = 1003
order2.products.append("Product D")

# Выводим информацию о заказах
print("Order 1:")
print(order1)
print("\nOrder 2:")
print(order2)
