'''
#4-2.辞書構造（dictionary）
4-2-2. 実践演習
下記のdictionaryオブジェクトを使用してそれぞれのkeyとvalueを取得し、
valueが20以上の場合{keyの中身}:hotと出力し、
超えていない場合は{keyの中身}:coldと出力せよ（目標２０分）
'''

'''
方法1
'''
temperatures = {'x': 24, 'y': 18, 'z': 30}
for key, value in temperatures.items():
    if value >= 20:
        print(key + ':hot')
    else:
        print(key + ':cold')

'''
方法2
'''
temperatures = {'x': 24, 'y': 18, 'z': 30}
for key, value in temperatures.items():
    if value >= 20:
        print(f'{key}:hot')
    else:
        print(f'{key}:cold')

'''
方法3
'''
temperatures = {'x': 24, 'y': 18, 'z': 30}
for key, value in temperatures.items():
    if value >= 20:
        S = "".join(key) + ':hot'
        print(S)
    else:
        S_2 = "".join(key) + ':cold'
        print(S_2)
