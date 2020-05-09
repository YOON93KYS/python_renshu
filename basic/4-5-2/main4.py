'''
4-5-2. 実践演習
１）ランダムな0~100の数値を20個生成しリストに格納せよ

２）リストの中身を2乗せよ（map)

３）リストから2000以下の数値を取り出して表示せよ(filter)

４）取り出した数値を全て合計して表示せよ(reduce)
'''
import random
a = []
for i in range(20):
    rand_int =random.randint(0, 100)
    a.append(rand_int)

a_2 = list(map(lambda x: x*x, a))
a_3 = list(filter(lambda x: x > 2000, a_2))

from functools import reduce
from operator import add
print(reduce(add, a_3));