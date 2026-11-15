# class User:
#     def __init__(self,name,second, age):
#         self.name=name
#         self.second = second
#         self.age=age
#     def __str__(self):
#         return f"""Name: {self.name}
# Second: {self.second}
# Age: {self.age}"""
# class Seller(User):
#     def __init__(self, name, second, age, rating):
#         super().__init__(name, second, age)
#         self.products={}
#         self.rating=rating
#     def add_product(self, name, qty):
#         if qty > 0:
#             self.products[name] = self.products.get(name, 0) + qty
#     def remove_product(self, name):
#         if name in self.products:
#             del self.products[name]
#             return True
#         return False
#     def update_stock(self, name, qty):
#         if name in self.products and self.products[name] + qty >= 0:
#             self.products[name] += qty
#             return True
#         return False
#     def get_stock(self):
#         return self.products.copy()
#     def __str__(self):
#         return f"""{super().__str__()}
# Rating: {self.rating}
# Products: {self.products}"""
# s1 = Seller("Ali", "Karimov", 25, 4.7)
# s1.add_product("Keyboard", 7)
# print(s1)