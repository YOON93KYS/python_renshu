'''
４）女性、30代で、50k以上の収入がある人を全て出力
'''
import pandas as pd
adult = pd.read_csv('adult.csv')

# 方法1(可読性悪い）

a = adult.gender == 'Female'
a_1 = adult.age >= 30
a_2 = adult.age < 40
a_3 = adult.income == '>50K'
print(adult[a & a_1 & a_2 & a_3])

# 方法2（可読性良い）

print(adult[
          (adult['gender'] == 'Female') &
          (adult['age'] >= 30) &
          (adult['age'] < 40) &
          (adult['income'] == '>50K')
      ])