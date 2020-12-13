nums = [i for i in range(10)]
print(nums)

nums = [i*i for i in range(10) if i % 2 == 0]
print(nums)

###########
nums = [i if i % 2 == 0 else i*i for i in range(10)]
print(nums)

nums=[]
for i in range(10):
    if i %2 == 0:
        nums.append(i)
    else:
        nums.append(i*i)

print(nums)