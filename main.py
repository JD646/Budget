import os
import pprint
import pandas as pd
import shutil
from scotia import scotia_visa, scotia_debit
from mint import mint
from td import td

#Open bank folder
os.chdir('bank')
x = os.listdir()

#list of csvs inside the bank folder
csvs = []

for file in x:
    if file.endswith('.csv'):
        csvs.append(file)        

#matching file to their respective class       
for file in csvs:
    if file.startswith('Scotia_Visa'):
        visa_path = file
        visa = scotia_visa(visa_path)
        visa.clean_up()
        visa_dict = {'Date': visa.fixed_date,
                     'Expenditure': visa.expenditure,
                     'Description': visa.fixed_name,
                     'Category': visa.category,
                     'Account': visa.account,
                     'Amount': visa.fixed_transaction}
        visa_df = pd.DataFrame(visa_dict)
        visa_df.to_csv('visa_processed.csv', index = False)
        shutil.move("/home/anubis/git/budget/bank/visa_processed.csv","/mnt/d/banking_files/visa_processed.csv")

    elif file.startswith('Scotia_Debit'):
        debit_path = file
        debit = scotia_debit(debit_path)
        debit.clean_up()
        debit_dict = {'Date': debit.fixed_date,
                     'Expenditure': debit.expenditure,
                     'Description': debit.fixed_name,
                     'Category': debit.category,
                     'Account': debit.account,
                     'Amount': debit.fixed_transaction}
        debit_df = pd.DataFrame(debit_dict)
        debit_df.to_csv('debit_processed.csv', index = False)
        shutil.move("/home/anubis/git/budget/bank/debit_processed.csv","/mnt/d/banking_files/debit_processed.csv")
    
    elif file.startswith('transactions'):
        mint_path = file
        mint = mint(mint_path)
        mint.clean_up()
        mint_dict = {'Date': mint.fixed_date,
                     'Expenditure': mint.expenditure,
                     'Description': mint.fixed_name,
                     'Category': mint.category,
                     'Account': mint.account,
                     'Amount': mint.fixed_transaction}
        mint_df = pd.DataFrame(mint_dict)
        mint_df.to_csv('mint_processed.csv', index = False)
        shutil.move("/home/anubis/git/budget/bank/mint_processed.csv","/mnt/d/banking_files/mint_processed.csv")
    
    elif file.startswith('td'):
        td_path = file
        td = td(td_path)
        td.clean_up()
        td_dict = {'Date': td.fixed_date,
                     'Expenditure': td.expenditure,
                     'Description': td.fixed_name,
                     'Category': td.category,
                     'Account': td.account,
                     'Amount': td.fixed_transaction}
        td_df = pd.DataFrame(td_dict)
        td_df.to_csv('td_processed.csv', index = False)
        shutil.move("/home/anubis/git/budget/bank/td_processed.csv","/mnt/d/banking_files/td_processed.csv")


print("Everything checks out chief, Files processed")