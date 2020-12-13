import random
lang = ['p','y','t','h','o','n']
random.shuffle(lang)

new_lang=''.join(lang)
print(new_lang)

char = random.choice(lang)
print(char)

#########
import math
x=3.14
print(math.floor(x))
print(math.ceil(x))

#########
import calculator
x = calculator.calc(3,4)
print(x)

y = calculator.differ(1,2)
print(y)