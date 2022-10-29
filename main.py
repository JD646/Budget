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
        shutil.move("/home/anubis/git/budget/bank/visa_processed.csv","/mnt/c/users/jonas/desktop/visa_processed.csv")

        #testcases
        #pprint.pprint(visa.fixed_date)
        #pprint.pprint(visa.fixed_name)
        #pprint.pprint(visa.fixed_transaction)
        #pprint.pprint(visa.expenditure)
        #pprint.pprint(visa.account)
        #pprint.pprint(visa.category)
        #pprint.pprint(visa_dict)

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
        shutil.move("/home/anubis/git/budget/bank/debit_processed.csv","/mnt/c/users/jonas/desktop/debit_processed.csv")

        #testcases
        #pprint.pprint(debit.fixed_date)
        #pprint.pprint(debit.fixed_name)
        #pprint.pprint(debit.fixed_transaction)
        #pprint.pprint(debit.expenditure)
        #pprint.pprint(debit.account)
        #pprint.pprint(debit.category)
        #pprint.pprint(debit_dict)
    
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
        shutil.move("/home/anubis/git/budget/bank/mint_processed.csv","/mnt/c/users/jonas/desktop/mint_processed.csv")

        #testcases
        #pprint.pprint(mint.fixed_date)
        #pprint.pprint(mint.fixed_name)
        #pprint.pprint(mint.fixed_transaction)
        #pprint.pprint(mint.expenditure)
        #pprint.pprint(mint.account)
        #pprint.pprint(mint.category)
        #pprint.pprint(mint_dict)
    
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
        shutil.move("/home/anubis/git/budget/bank/td_processed.csv","/mnt/c/users/jonas/desktop/td_processed.csv")

        #testcases
        #pprint.pprint(td.fixed_date)
        #pprint.pprint(td.fixed_name)
        #pprint.pprint(td.fixed_transaction)
        #pprint.pprint(td.expenditure)
        #pprint.pprint(td.account)
        #pprint.pprint(td.category)
        #pprint.pprint(td_dict)


print("Everything checks out chief")