names = ["Ali", "Valijon", "Sami", "Diyorbek"]

a = lambda a : len(a)

b = max(names, key=a)
print(b)