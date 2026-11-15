# class Person:
#     def __init__(self, name, id_number):
#         self.name=name
#         self.id_number=id_number
#     def __str__(self):
#         return f"""Name: {self.name}
# ID: {self.id_number}"""
# class Patient(Person):
#     def __init__(self, name, id_number):
#         super().__init__(name, id_number)
#         self.diagnoses = []
#         self.bill= 0
#     def add_diagnosis(self, text):
#         self.diagnoses.append(text)
#     def add_charge(self, amount):
#         if amount > 0:
#             self.bill += amount
#     def pay(self, amount):
#         if amount > 0:
#             self.bill-= amount
#             if self.bill<0:
#                 self.bill = 0
#             return True
#         return False
#     def get_balance(self):
#         return self.bill
#     def print_history(self):
#         print("Diagnoses:", self.diagnoses)
#         print("Balance:", self.bill)
#     def __str__(self):
#         return f"""{super().__str__()}
# Diagnoses: {self.diagnoses}
# Bill: {self.bill}"""
# p1 = Patient("Ali", "12345")
# p1.add_diagnosis("Gripp")
# p1.add_diagnosis("Shamollash")
# p1.add_charge(200000)
# p1.pay(250000)
# print(p1)
# p1.print_history()