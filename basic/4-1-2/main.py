'''
4-1-2. 実践演習
1〜10までをリストに格納し、それぞれの値を2乗した値を出力せよ（目標１０分）
'''

'''
方法1
'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for value in x:
    print(value * value)

'''
#方法2
'''
x_2 = [i + 1 for i in range(10)]

for value_2 in x_2:
    print(value_2 * value_2)

'''
#方法３
'''

x_3 = list(range(1, 11))
for value_3 in x_2:
    print(value_3 * value_3)
