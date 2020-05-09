'''
7-1-1. 演習問題
1から100までの数を出力するプログラムを書け。
ただし3の倍数のときは数の代わりに｢Fizz｣と、5の倍数のときは｢Buzz｣と出力し、3と5両方の倍数の場合には｢FizzBuzz｣と出力せよ。
'''
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
