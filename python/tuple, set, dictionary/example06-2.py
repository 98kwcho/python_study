import random

ranNum = random.randint(1, 10)

dic = {x : x*x for x in range(1, ranNum)}

print(dic)