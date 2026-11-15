# class Course:
#     """Asosiy (parent) klass."""
#     def __init__(self, title: str, instructor: str):
#         self.title = title
#         self.instructor = instructor
#         self.students: list[str] = []
#     def enroll(self, student_name: str) -> bool:
#         if student_name in self.students:
#             return False
#         self.students.append(student_name)
#         return True
#     def get_room(self) -> str:
#         return "Room: not assigned"
#     def __str__(self) -> str:
#         return f"Course: {self.title} ({self.instructor})"
# class OnlineCourse(Course):
#     def __init__(self, title: str, instructor: str, url: str, max_students: int):
#         super().__init__(title, instructor)
#         self.url = url
#         self.max_students = max_students
#     def enroll(self, student_name: str) -> bool:
#         if len(self.students) < self.max_students and student_name not in self.students:
#             self.students.append(student_name)
#             return True
#         return False
#     def get_room(self) -> str:
#         return f"Virtual: {self.url}"
# class OfflineCourse(Course):
#     def __init__(self, title: str, instructor: str, room: str, capacity: int):
#         super().__init__(title, instructor)
#         self.room = room          # auditoriya/xona raqami, masalan "B-203"
#         self.capacity = capacity  # maksimal talaba soni
#     def enroll(self, student_name: str) -> bool:
#         if len(self.students) < self.capacity and student_name not in self.students:
#             self.students.append(student_name)
#             return True
#         return False
#     def get_room(self) -> str:
#         return f"Room: {self.room}"
# if __name__ == "__main__":
#     o = OnlineCourse("Python Basics", "Guzal", url="https://nt.uz/py", max_students=2)
#     print(o.enroll("Ali"))      # True
#     print(o.enroll("Vali"))     # True
#     print(o.enroll("Karim"))    # False (to'ldi)
#     print(o.get_room())         # Virtual: https://nt.uz/py
#     f = OfflineCourse("Algorithms", "Dilshod", room="B-203", capacity=1)
#     print(f.enroll("Soliha"))   # True
#     print(f.enroll("Nodir"))    # False
#     print(f.get_room())         # Room: B-203
#     print(f)                    # Course: Algorithms (Dilshod)