with open('sample.txt', mode='r+') as f:
    print(f.tell())
    data = f.read()
    print(f.tell())
    #f.write('Good morning\n')
    print(f.tell())
    f.seek(10)
    data2 = f.read()
    print(data2)