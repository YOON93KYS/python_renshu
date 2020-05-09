'''
６）レコードからランダムに3つ取り出してレコード内容を表示せよ
'''
import pandas as pd
adult = pd.read_csv('adult.csv')

print(adult.sample(3))
