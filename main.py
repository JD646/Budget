import pandas

Date = 0
Name = 1
Transaction = 2

### CSV reader ###

df = pandas.read_csv('pcbanking.csv',
                    names=['Date','Name','Transaction'])

print(df)
print(type(df))