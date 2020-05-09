'''
4-6-2. 実践演習
１）ランダムな0~100の数値を10個生成しリストに格納せよ

２）それぞれの数値を2乗し、出力せよ

'''

import random
a = []
for i in range(10):
    rand_int =random.randint(0, 100)
    a.append(rand_int)

a_2 = [x*x for x in a]
print(a_2) #[8, 10]