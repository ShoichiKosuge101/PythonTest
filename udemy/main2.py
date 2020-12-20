def is_Even(num):
        return num %2 == 0

print(is_Even(2))
print(is_Even(5))

nums = map(int,['1','2','3','4'])
#even_nums = filter(is_Even,nums)
even_nums = filter(lambda x: x%2 == 0,nums)
print(even_nums)
print(list(even_nums))
