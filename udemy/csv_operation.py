import csv

data = '''11 12 13 14
21 22 23 24
31 32 33 34
'''

with open('sample.csv',mode ='r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        print(row)
    #f.write(data)
