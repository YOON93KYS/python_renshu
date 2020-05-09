'''
８）上記のファイルをさらにjsonとしてファイルに書き出せ
'''
import pandas as pd
adult = pd.read_csv('adult.csv')
adult[['gender', 'age']].to_json('test.json')

