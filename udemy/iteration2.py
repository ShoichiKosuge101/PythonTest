weight = 70

while weight >= 50:
    weight -= 1
    print(weight)

count = 0
score = 80

while count < 100:
    if count < 50:
        count += 1
        continue
    print(count)
    count += 1
    if count == score:
        print(score)
        break
