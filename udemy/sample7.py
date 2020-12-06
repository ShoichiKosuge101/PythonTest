# 集合型

hands = {'グー','グー','グー','チョキ','チョキ'}

print(hands,type(hands))
print(len(hands))
#print(hands[0])
print(list(hands)[0])

print(set([1,2,3]))
hands.add('パー')
print(hands)
hands.discard('チー')
hands.discard('チョキ')
#hands.remove('チー')
hands.remove('パー')
print(hands)


A={1,2,3}
B={3,4,5}

print(A|B)
print(A&B)

C={7,8,9,10}

print(A&C)

print(A-B)
print({1,2,3}-{1,2,4})

print((A|B)-(A&B))
print(A^B)