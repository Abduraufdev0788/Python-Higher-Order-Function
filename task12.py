students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]
sorted_list = list(sorted(students, key=lambda students:students['grade'], reverse=False))

print(sorted_list)