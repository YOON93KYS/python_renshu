'''
１）2つの整数を引数に受け取り、その2つの数の最大公約数を返すプログラムを書け（目標６０分）
'''
x = int(input('整数を入れてください'))
y = int(input('整数を入れてください'))


def abc(x, y):
    if x % y == 0:
        return y
    else:
        return abc(y, x % y)


print(abc(x, y))
