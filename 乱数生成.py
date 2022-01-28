import random

A = int(input('生成する乱数の数: '))
B = int(input('最小値: '))
C = int(input('最大値: '))
X = 0
while X < A:
    X = X + 1
    print(random.randint(B, C))
