num = [0,1,2]

try:
    a = 1/0
    print(a)
    print(num[3])
#except (IndexError, ZeroDivisionError) as e:
#    print(e)
#    print(type(e))
#    print('例外が発生しました')
#except ZeroDivisionError as ee:
    #print(ee)
    #print(type(ee))
    #print('0で割り切れない')
except Exception as e:
    print(e)
    print(type(e))
    print('どんな例外もキャッチ')

print('Finish.')