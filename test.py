import random

names = ['Krisna', 'ram', 'rohan', 'lisa', 'sani']

new_dict = { student:random.randint(1, 100) for student in names }
passed_students = { student: score for (student, score) in new_dict.items() if score > 50}
print(new_dict)
print(passed_students)