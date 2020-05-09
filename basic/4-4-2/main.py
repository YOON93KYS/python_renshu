'''
4-4-2. 実践演習
ランダムに1~100の値を100個生成し、生成された数値を1度ずつ表示せよ。（目標１５分）
'''
import random

for i in range(100):
    rand_int = random.randint(1, 100)
    print(rand_int)
