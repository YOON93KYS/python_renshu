'''
３）データセットの中で男性の割合(%)を出力
'''
import pandas as pd
adult = pd.read_csv('adult.csv')

print(len(adult[adult.gender == 'Male']) * 100 / len(adult))
