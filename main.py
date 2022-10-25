import pandas as pd
import pprint
from config import Configuration

#Creating a dataframe out of the CSV file
df = pd.read_csv('pcbanking.csv',
                    names=['Date','Name','Transaction'])

#Creation of lists
date = df['Date'].values.tolist()
name = df['Name'].values.tolist()
transaction = df['Transaction'].values.tolist()

##FIXING OVERALL LIST FORMAT

#Fixing date format
fixed_date = []
for entry in date:
    seperated = entry.split("/")
    if len(seperated[Configuration.MONTH]) == 1:
        fixed_m = '0' + seperated[Configuration.MONTH]
        seperated[Configuration.MONTH] = fixed_m
    if len(seperated[Configuration.DAY])== 1:
        fixed_d = '0' + seperated[Configuration.DAY]
        seperated[Configuration.DAY] = fixed_d
    if len(seperated[Configuration.YEAR]) == 4:
        fixed_y = seperated[Configuration.YEAR][2:]
        seperated[Configuration.YEAR] = fixed_y

    seperated[Configuration.MONTH], seperated[Configuration.DAY] = seperated[Configuration.DAY], seperated[Configuration.MONTH]
    entry = "/".join(seperated)
    fixed_date.append(entry)

#Fixing transaction format
fixed_transaction = []
expenditure = []

for cost in transaction:
    cost = float(cost)
    if cost < 0:
        cost = cost * -1
        cost = format(cost, '.2f')
        fixed_transaction.append(cost)
        expenditure.append("Out")
    elif cost >= 0:
        cost = format(cost, '.2f')
        fixed_transaction.append(cost)
        expenditure.append("In")

#Fixing naming format
fixed_name = []
for description in name:
    description = description.strip()
    description = description.rstrip("(GOOGLE PAY)")

    description = description.rstrip("ON")
    description = description.rstrip("BC")
    description = description.rstrip("AB")
    description = description.rstrip()

    description = description.rstrip("MISSISSAUGA")
    description = description.rstrip("TORONTO")
    description = description.rstrip("ETOBICOKE")
    description = description.rstrip("VANCOUVER")
    description = description.rstrip()
    
    fixed_name.append(description)

pprint.pprint(fixed_name)



