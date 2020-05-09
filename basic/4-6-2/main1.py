'''
4-6-2. 実践演習
１）ランダムな0~100の数値を10個生成しリストに格納せよ

２）それぞれの数値を2乗し、出力せよ

'''
import random
'''
#1)ランダムな0~100の数値を10個生成しリストに格納せよ
'''
a = []
for i in range(10):
    rand_int = random.randint(0, 100)
    a.append(rand_int)
