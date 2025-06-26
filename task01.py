numbers = [4, -2, 0, 7, -9, 3, -1, 5]

def positive_numbers(nums):
    if nums >= 0:
        return nums
    
a = filter(positive_numbers, numbers)

print(list(a))
    