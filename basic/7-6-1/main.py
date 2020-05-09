'''
7-6-1. 演習問題
円周率の近似値を求める方法として、乱数を使う方法がある。

今回は下記のように1×1の四角のなかにランダムに点を打ち、その点を大量に打つことで円周率を求める。

(0,0)の座標からの距離が1よりも小さい点の数と1よりも大きい点の数を比較することで、下記のように円周率を求めることが出来る。

そのプログラムを書け。

円周率 = 4 *(距離が1よりも小さい点の数) / (全ての点の数)

#0~1.0の範囲の擬似乱数の生成
import random
random.random()
'''
import random


n = 1000
count = 0
for i in range(n):
    x = random.random()
    y = random.random()
    if (x * x + y * y < 1):
        count = count + 1
a = 4 * count / n
print(a)
