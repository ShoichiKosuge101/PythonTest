import csv

nums = [
    [11,12,13,44],
    [21,22,23,24],
    [31,32,33,34]
]

header = ['','ONE','TWO','THREE','FOUR']
index = ['one','two','three','four']

with open('sample.csv',mode='w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i,row in zip(index, nums):
        writer.writerow([i]+ row)
    f.seek(0)
    print(f.read())
