from random import randint
# rrr = lambda x: list((range(0,x)))
# print(rrr(100))

rrr = lambda x,y: list(range(x,randint(1, y)))
print(rrr(10,100))