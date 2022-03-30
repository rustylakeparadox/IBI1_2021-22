import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/undergraduate/IBI")
os.getcwd()
os.listdir()

covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
covid_data.info()
covid_data.describe()
covid_data.iloc[0,1]
covid_data.iloc[2,0:5]
covid_data.iloc[0:2,:]
covid_data.iloc[0:10:2,0:5]
covid_data.iloc[0:3,[0,1,3]]
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3,my_columns]
covid_data.loc[2:4,"date"]

print(covid_data.loc[covid_data['location']=='Afghanistan','total_cases'])


china_new_data=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]

new_cases_mean=np.mean(china_new_data['new_cases'])
print(new_cases_mean)

new_deaths_mean=np.mean(china_new_data['new_deaths'])
print(new_deaths_mean)

plt.boxplot(china_new_data['new_cases'],vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.show()
plt.boxplot(china_new_data['new_deaths'],vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.show()

plt.plot(china_new_data['date'], china_new_data['new_cases'], 'b+')
plt.show()

plt.plot(china_new_data['date'], china_new_data['new_cases'], 'bo', china_new_data['date'], china_new_data['new_deaths'], 'ro',scalex = 'date', scaley ='number' )
plt.xticks(china_new_data['date'].iloc[0:len(china_new_data['date']):4],rotation=-90)
plt.legend(('new cases', 'new deaths'), loc = 'upper right')
plt.title('total cases and deaths in China')
plt.show()

March_14_cases = covid_data.loc[covid_data['date'] == '2020-03-13', ['total_cases']]
plt.boxplot(March_14_cases['total_cases'], vert = True, whis = 1.5, patch_artist = True, meanline = False, showbox=True,showcaps=True,showfliers=True,notch=False)
plt.show()
