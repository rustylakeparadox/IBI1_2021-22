# import all the packages needed
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# set the working directory
os.chdir("D:/undergraduate/IBI")
# print out the working directory 
os.getcwd()
# list all the directories 
os.listdir()

# import the 'full_data.csv' file
covid_data = pd.read_csv("full_data.csv")
# output the first 5 rows of the dataset
covid_data.head(5)
# output some basic information about 'covid_data', including the data type, the column names, the number of rows and columns, the memory usage ...
covid_data.info()
# output some statistical characteristics about 'covid_data', including the number of entries, mean, standard deviation and a number of quantiles.
covid_data.describe()

# show the first and third columns from rows 10-20 (inclusive)
covid_data.iloc[10:21, [1,3]]

# use a Boolean to print out “total cases” for all rows corresponding to Afghanistan
print(covid_data.loc[covid_data['location']=='Afghanistan','total_cases'])

# use a Boolean to find the value of "new cases" and "new deaths" in China, and input it as a new dataset
china_new_data=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]

# compute the mean number of new cases and new deaths in China and print out the outcomes
# use np.mean to caculate the mean value
new_cases_mean=np.mean(china_new_data['new_cases'])
print(new_cases_mean)
new_deaths_mean=np.mean(china_new_data['new_deaths'])
print(new_deaths_mean)

# create a new data set to store the value of new cases and new deaths in China
a = china_new_data.loc[:,['new_cases','new_deaths']]
# use plt.boxplot to draw the boxplot
plt.boxplot(a,vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=False,notch=False)

#  plot both new cases and new deaths in China over time
plt.plot(china_new_data['date'], china_new_data['new_cases'], 'bo', china_new_data['date'], china_new_data['new_deaths'], 'ro',scalex = 'date', scaley ='number' )
# adjust the graph
plt.xticks(china_new_data['date'].iloc[0:len(china_new_data['date']):4],rotation=-90)
# add the legends to the graph to indicate some
plt.legend(('new cases', 'new deaths'), loc = 'upper right')
# add the title
plt.title('total cases and deaths in China')
# show the graph
plt.show()

# find the total case numbers in different countries on 14 March 2020 and save them in a new dataset
March_14_cases = covid_data.loc[covid_data['date'] == '2020-03-13', ['total_cases']]
# draw the boxplot 
plt.boxplot(March_14_cases['total_cases'], vert = True, whis = 1.5, patch_artist = True, meanline = False, showbox=True, showcaps=True, showfliers=True, notch=False)
# show the graph
plt.show()
