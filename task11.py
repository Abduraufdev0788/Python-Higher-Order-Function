nums = list(range(1, 21))

def pair_nums(num):
    if num % 2 ==0:
        return num

a = list(filter(pair_nums, nums))

degree = list(map(lambda x : x * x, a))

print(degree)