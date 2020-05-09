'''
２）データセットの年齢の合計値を出力
'''
import pandas as pd
adult = pd.read_csv('adult.csv')

print(adult['age'].sum())
