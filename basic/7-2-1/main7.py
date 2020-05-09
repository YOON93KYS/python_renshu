'''
７） 性別・年齢の項目以外を消去したデータにし、csvに書き出せ
'''
import pandas as pd
adult = pd.read_csv('adult.csv')
adult[['gender', 'age']].to_csv('test.csv')
