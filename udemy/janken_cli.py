import random

hands = ['グー','チョキ','パー']

win,draw,lose = '勝ち','あいこ','負け'
rules={
    (0,0): draw, (0,1): win, (0,2): lose,
    (1,0): lose, (1,1): draw, (1,2): win,
    (2,0): win, (2,1): lose, (2,2): draw,
}

while True:
    my_hand = int(input(
'''0～2の数字を入力してください。
0:グー,1:チョキ,2:パー,9:End
>>>'''))

    if my_hand in range(0,3):
        enemy_hand = random.randint(0,2)
        print('You:',hands[my_hand],'  Enemy:', hands[enemy_hand])
        result = rules[(my_hand, enemy_hand)]
        print(result)
        if my_hand != enemy_hand:
            break
    elif my_hand == 9:
        break
    else:
        print('err')
        break