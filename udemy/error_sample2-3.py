class TemperatureRangeError(Exception):
    pass


try:
    body_temperature = float(input())
except ValueError:
    print('体温は数値を入力してください')
    exit()

if body_temperature < 34 or body_temperature > 44:
    raise TemperatureRangeError('異常な体温です。もう一度入力してください')
elif body_temperature < 37.5:
    print('正常です')
else:
    print('熱があります。検査を受けてください')