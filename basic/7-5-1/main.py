'''
以下のように前の2つの数を足した数の列をフィボナッチ数列という。
1 1 2 3 5 8 13 21 34 55 89 144 …
この数列を100番目まで表示せよ。
'''


def abc(x):
    if x >= 2:
        return abc(x - 1) + abc(x - 2)
    else:
        return x


for x in range(1, 101):
    print(x, abc(x))
