# read in a log file
# Author: Andrew Beatty
# Reproduced by Elaine Cazetta

import pandas as pd
import re
import matplotlib.pyplot as plt


def clearSqrBrackets(string):
    return 

path = './data/'
logFilename = path + 'access.log.demo'

colNames= ('ip',
    'dash1', 
    'userId', 
    'time', 
    'url', 
    'status code', 
    'size of response', 
    'referer', 
    'user agent', 
    'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

print(df)

# drop columns
df.drop(columns=['dash1', 'userId'], inplace=True)

# remove the [] from time
# there is a lot in this line 
# apply with apply the function to each element in the column and return a series
# which I make the column equal to

df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
# for the task you may want to use a normal function instead of lambda
'''
def getNewValue(x):
    newvalue = re.search('[\w:/]+', x).group()
    # do your stuff
    return newvalue

df['time'] = df['time'].apply(getNewValue)
'''


# this is not a normal date time format so we need to specify it
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html?highlight=to_datetime
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
print (df.dtypes)
# output row of id 0
print(df.iloc[0])

start_date = pd.to_datetime('2021/02/15 23:00')
end_date = pd.to_datetime('2021/02/15 23:59:59')


# see
# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/09_timeseries.html
# for more info on dealing with time
# way one use the loc function 
#newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]
# way 2 use the series function between
#newdf = df[df.time.between(start_date, end_date)]
# way three set the index to the date column
# this give a whole pile of handy features
df = df.set_index(['time'])
newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
#newdf = df.between_time('23:00', '23:59') # this is times every day
print (newdf)

# sample the download sizes say every 30 Minutes
downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)

# more information on the documents
# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/04_plotting.html
downloadSamples.plot()
plt.show()

# get the rolling mean of responses