import csv

num_rows =[
    ['11','12','13','14'],
    ['21','22','23','24'],
    ['31','32','33','34']
]

with open('sample.csv','a+', newline='') as f:
    writer = csv.DictWriter(f, fieldnames = ['ONE','TWO','THREE','FOUR'])
    writer.writerow({'FOUR':41,'TWO':42,'THREE':43,'ONE':44})
    f.seek(0)
    reader = csv.DictReader(f, fieldnames=['ONE','TWO','THREE','FOUR'])
    for row in reader:
        print(row['ONE'])