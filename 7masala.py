# class Course:
#     def __init__(self,title,teacher):
#         self.title=title
#         self.teacher=teacher
#         self.students=[]
#     def get_title(self):
#         return self.title
#     def get_teacher(self):
#         return self.teacher
#     def enroll(self, student_name):
#         if student_name not in self.students:
#             self.students.append(student_name)
#             return True
#         return False
#     def drop(self, student_name):
#         if student_name in self.students:
#             self.students.remove(student_name)
#             return True
#         return False
#     def __str__(self):
#         return f"Course: {self.title} ({self.teacher})"
# c1 = Course("Python Basics", "Guzal")
# c1.enroll("Ali")
# c1.enroll("Vali")
# print(c1)
# print(c1.students)