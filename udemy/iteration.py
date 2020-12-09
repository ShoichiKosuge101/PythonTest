scores = [55,43,78,38,96,51]

for i in range(len(scores)):
    print(scores[i])

for score in scores:
    if score >= 80:
        print(str(score) + '点:'+ '合格')
    else:
        print(str(score) + '点:' + '不合格')

for x in range(1,10):
    for y in range(1,10):
        print(str(x) + 'x' + str(y) + '=' + str(x * y))