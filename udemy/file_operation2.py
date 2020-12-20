with open('sample.txt', mode='r') as f:
    #f.write('Good morning\n')
    #f.write('Good afternoon\n')
    #f.write('Good evening\n')
    #data = f.read()
    lines = f.readlines()
    print(type(lines))
    print(lines)
    for line in lines:
        print(line, end='')

#print(data)
