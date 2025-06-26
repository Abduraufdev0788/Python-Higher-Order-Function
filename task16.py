data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

a = list(sorted(data, key=lambda x : str(x) and len(x) > 5))

print(a)
# STRlarni jaratib olishni bilmadim