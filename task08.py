people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]
sorted_list = list(sorted(people, key=lambda people:people['age'], reverse=True))

print(sorted_list)