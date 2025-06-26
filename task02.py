nums = [1, 2, 3, 4, 5]

def degree(n):
    return n ** 2
num_list = map(degree, nums)

print(list(num_list))