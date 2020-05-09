'''
５）4）のデータを別名でcsvファイルとして書き出す
'''
import pandas as pd
adult = pd.read_csv('adult.csv')

# 方法1　データフレームの書き方が一般的ではない
a = adult.gender == 'Female'
a_1 = adult.age >= 30
a_2 = adult.age < 40
a_3 = adult.income == '>50K'
adult[a & a_1 & a_2 & a_3].to_csv('test.csv')

# 方法2 可読性良い
adult[
    (adult['gender'] == 'Female') &
    (adult['age'] >= 30) &
    (adult['age'] < 40) &
    (adult['income'] == '>50K')
    ].to_csv('test2.csv')
