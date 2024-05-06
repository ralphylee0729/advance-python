def multiply_by_2(x: int) -> int:
    return x * 2

mixlist = [0,1,2,3,"oo","pp",99]
nums = [1,2,3,4,5]

double_nums_map = map(multiply_by_2, nums)

#triple_nums = , nums)

# invalid: no random access for map object
# print(f'num={double_nums[0]}')

for num in double_nums_map:
    print(f'num={num}')

double_num_list = list(map(lambda x: x *2, nums))

print(double_num_list)
