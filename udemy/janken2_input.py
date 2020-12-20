import random
hands = ['グー','チョキ','パー']

#i = random.randint(0,2)
#hand = hands[i]
#print(hand)

my_input = input('0~2の数字を入力してください>>>')
print(my_input)
i = int(my_input)
if i in range(0,3):
    hand = hands[i]
    print(hand)
else:
    print('error')