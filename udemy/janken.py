hands = ['guu','choki','paa']
hands2 = {'0':'guu','1':'choki','2':'paa'}
gu , choki, pa = 'グー','チョキ','パー' #タプル
win, draw, lose = '勝ち','あいこ','負け'

my_hand = choki
enemy_hand = choki

if my_hand == enemy_hand:
    print(draw)
elif (my_hand == gu and enemy_hand == choki) or \
    (my_hand == pa and enemy_hand == gu) or \
    (my_hand == choki and enemy_hand == pa)    :
    print(win)
else:
    print(lose)
