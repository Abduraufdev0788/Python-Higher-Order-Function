text = ["apple", "34", "banana", "100", "abc", "75"]

def numeric_table(nums:str):
    if nums.isnumeric():
        return nums
    
Num_list = list(filter(numeric_table, text))

print(Num_list)