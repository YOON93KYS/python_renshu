'''
1000までの素数を全て表示せよ（目標６０分）
'''
x = 1000


def abc(x):
    if x == 1:
        return False
    if x == 0:
        return False
    for a in range(2, x):
        if x % a == 0:
            return False
    else:
        return True


for i in range(x+1):
    if (abc(i)):
        print(i)