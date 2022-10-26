import pandas as pd
import pprint
import sys
from config import Configuration
from scotia import scotia_visa
from scotia import scotia_debit

file_path = sys.argv[1]


# #Creating a dataframe out of the CSV file
# df = pd.read_csv(file_path,
#                     names=['Date','Name','Transaction'])

# #Creation of lists
# date = df['Date'].values.tolist()
# name = df['Name'].values.tolist()
# transaction = df['Transaction'].values.tolist()

visa = scotia_visa(visa_path)
visa.clean_up()

debit = scotia_debit(debit_path)
debit.clean_up()
#s_debit = scotia_debit(date, transaction, name)

pprint.pprint(visa.fixed_date)
