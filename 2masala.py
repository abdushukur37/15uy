# class User:
#     def __init__(self, name, email, address):
#         self.name=name
#         self.email=email
#         self.address=address
# class Customer(User):
#     def __init__(self, name, email, address, balance):
#         super().__init__(name, email, address)
#         self.cart = []
#         self.balance = balance
#     def add_to_cart(self, product, qty, price):
#         if qty > 0 and price >= 0:
#             self.cart.append((product, qty, price))
#     def clear_cart(self):
#         self.cart = []
#     def get_cart_total(self):
#         return sum(qty * price for product, qty, price in self.cart)
#     def checkout(self):
#         jami = self.get_cart_total()
#         if self.balance >= jami:
#             self.balance -= jami
#             self.clear_cart()
#             return True
#         return False
#     def __str__(self):
#         return f"Customer: {self.name} (balance: {self.balance} so'm)"
# c = Customer("Ali", "ali@gmail.com", "Toshkent", 500000)
# c.add_to_cart("Telefon", 1, 300000)
# c.add_to_cart("Naushnik", 2, 50000)
# print(c.get_cart_total())
# print(c.checkout())
# print(c)