# class Person:
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number
#     def get_name(self):
#         return self.name
#     def get_id(self):
#         return self.id_number
#     def __str__(self):
#         return f"Person: {self.name} (#{self.id_number})"
# class Patient(Person):
#     def __init__(self, name, id_number):
#         super().__init__(name, id_number)
#         self.diagnoses = []
#         self.bill = 0
#     def add_diagnosis(self, text):
#         self.diagnoses.append(text)
#     def add_charge(self, amount):
#         if amount > 0:
#             self.bill += amount
#     def pay(self, amount):
#         if amount > 0:
#             self.bill -= amount
#             if self.bill < 0:
#                 self.bill = 0
#             return True
#         return False
#     def get_balance(self):
#         return self.bill
#     def print_history(self):
#         print(f"🧑‍⚕️ Bemor: {self.name} (#{self.id_number})")
#         print("Tashxislar tarixi:")
#         for i in range(len(self.diagnoses)):
#             print(f"  {i+1}. {self.diagnoses[i]}")
#         print(f"Joriy qarzdorlik: {self.bill} so'm")
# class Doctor(Person):
#     def __init__(self, name, id_number, specialty):
#         super().__init__(name, id_number)
#         self.specialty = specialty
#         self.schedule = {}
#     def add_slot(self, day, time):
#         if day not in self.schedule:
#             self.schedule[day] = []
#         if time not in self.schedule[day]:
#             self.schedule[day].append(time)
#     def book_slot(self, day, time):
#         if day in self.schedule and time in self.schedule[day]:
#             self.schedule[day].remove(time)
#             return True
#         return False
#     def available_slots(self, day):
#         if day in self.schedule:
#             return self.schedule[day].copy()
#         return []
#     def __str__(self):
#         return f"Dr. {self.name} ({self.specialty})"
# p = Patient("Aziz", "AB1234567")
# p.add_diagnosis("ORVI")
# p.add_charge(150000)
# p.add_charge(80000)
# print(p.get_balance())
# p.pay(100000)
# print(p.get_balance())
# p.print_history()
# d = Doctor("Gulrux", "CD7654321", specialty="Cardiologist")
# d.add_slot("Mon", "09:00")
# d.add_slot("Mon", "09:30")
# print(d.book_slot("Mon", "09:00"))
# print(d.book_slot("Mon", "09:00"))
# print(d.available_slots("Mon"))
# print(d)