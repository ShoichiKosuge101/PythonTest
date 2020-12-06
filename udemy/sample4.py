my_friends = ['花子','太郎','健太','瞳']
print(my_friends,type(my_friends))
print(my_friends[1])
my_friends[1]='次郎'
print(my_friends[1])

a=[1,2,3]
b=[4,5,6]

c=[a,b]
print(c)
print(c[0][2])

a=[0,1,2,3,4]
print(len(a))

a=['a','b','c']
a.append(4)
print(a)
a.insert(0,'z')
print(a)
print(a.pop())
print(a)
print(a.remove('a'))
print(a)

num_list=[20,50,33,77,15]
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
print(77 in num_list)
name_list = ['My','name','is','Ken']
print(name_list)
print(' '.join(name_list))
print(name_list)
print('-'.join(name_list))

print('My name is Ken'.split())
print('My name is Ken'.split('e'))