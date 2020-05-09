'''
９）ageとhours-per-weekの関係について散布図を表示せよ
'''
import pandas as pd
from matplotlib import pyplot as plt
adult = pd.read_csv('adult.csv')

adult.plot(kind='scatter', x='age', y='hours-per-week')
plt.show()
