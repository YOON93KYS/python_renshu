'''
１）データセットの年齢の平均値を出力
'''
import pandas as pd
adult = pd.read_csv('adult.csv')

print(adult['age'].mean())
