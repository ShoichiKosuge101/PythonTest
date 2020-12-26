def double(num):
    if not isinstance(num,int):
        raise TypeError(f'double関数には整数型の値を渡してください。{type(num)}が入力されています')
    return num * 2

#a = double(lambda x: x ** 2)
a = double(1)
print(a)

