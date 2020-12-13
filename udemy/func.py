s = [2,4,5,7,9]
t='japanese'

print(len(s),len(t))
#############
x = print()
print(x)

#############
def add(a,b=100):
    return a + b

c = add(10,6)
print(c)

d = add(2)
print(d)

e = add(b=10,a=2)
print(e)

###############
def say_hello():
    print('Hello')

say_hello()
