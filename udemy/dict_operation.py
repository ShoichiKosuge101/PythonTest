import csv
num_rows = [
    ['11','12','13','14'],
    ['21','22','23','24'],
    ['31','32','33','34']
]

with open('sample.csv', mode='w+',newline='') as f:
    writer = csv.writer(f)
    for row in num_rows:
        writer.writerow(row)
    f.seek(0)
    reader = csv.DictReader(f, fieldnames=['ONE','TWO','THREE','FOUR'])
    for row in reader:
        print(row)
