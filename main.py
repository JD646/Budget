import os
import pandas as pd
import pprint
import sys
from config import Configuration
from scotia import scotia_visa, scotia_debit


os.chdir('bank')
x = os.listdir()
csvs = []

for file in x:
    if '.csv' in file:
        csvs.append(file)
        

for file in csvs:
    if 'Scotia_Visa' in file:
        visa_path = file
        visa = scotia_visa(visa_path)
        visa.clean_up()


    elif "Scotia_Debit" in file:
        debit_path = file
        debit = scotia_debit(debit_path)
        debit.clean_up()

#testcases
pprint.pprint(visa.fixed_date)
pprint.pprint(visa.fixed_name)
pprint.pprint(debit.fixed_date)
pprint.pprint(debit.fixed_name)