prices = ["$120", "$340", "$50", "$90"]
a = list(map(lambda a : int(a.replace("$", "")), prices))

print(a)