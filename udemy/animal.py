class Animal:

    def __init__(self,kind,age):
        self.kind = kind
        self.age = str(age) + '歳'

    def cry(self):
        print('私は'+ self.kind + 'です')


class Dog(Animal):
    pass

class Cat(Animal):
    
    def __init__(self,kind,age,color):
        super().__init__(kind,age)
        self.color = color

    def cry(self):
        print('にゃーん、'+self.kind+'だみゃお。'+'色は'+self.color+'だみゃん')

pochi = Animal("犬",5)
Shiba = Dog('秋田犬',8)
tama = Cat("ぶち猫",3,'黒')
print(pochi.kind, pochi.age)
print(tama.kind, tama.age)
#print("Animal Count",Animal.count)


pochi.cry()
Shiba.cry()
tama.cry()

#Shiba.run()

#pochi = Animal()
#tama = Animal()
#print(type(pochi))
#print(type(tama))
#print(pochi is tama)