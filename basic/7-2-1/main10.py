'''
１０）ageを10代毎に区切り、ヒストグラムを表示せよ
'''
import pandas as pd
from matplotlib import pyplot as plt
adult = pd.read_csv('adult.csv')

adult.plot(kind='hist', y=['age'], range=(0, 100), bins=10)
plt.show()