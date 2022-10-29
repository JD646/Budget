import os
import pprint
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
        # visa_dict = {'Date': visa.fixed_date,
        #              'Expenditure': visa.expenditure,
        #              'Description': visa.fixed_name,
        #              'Category': visa.category,
        #              'Account': visa.account,
        #              'Amount': visa.transaction}

        #testcases
        #pprint.pprint(visa.fixed_date)
        #pprint.pprint(visa.fixed_name)
        #pprint.pprint(visa.fixed_transaction)
        #pprint.pprint(visa.expenditure)
        #pprint.pprint(visa.account)

    elif file.startswith('Scotia_Debit'):
        debit_path = file
        debit = scotia_debit(debit_path)
        debit.clean_up()

        #testcases
        #pprint.pprint(debit.fixed_date)
        #pprint.pprint(debit.fixed_name)
        #pprint.pprint(debit.fixed_transaction)
        #pprint.pprint(debit.expenditure)
        #pprint.pprint(debit.account)
        pprint.pprint(debit.category)
    
    elif file.startswith('transactions'):
        mint_path = file
        mint = mint(mint_path)
        mint.clean_up()

        #testcases
        #pprint.pprint(mint.fixed_date)
        #pprint.pprint(mint.fixed_name)
        #pprint.pprint(mint.fixed_transaction)
        #pprint.pprint(mint.expenditure)
        #pprint.pprint(mint.account)
    
    elif file.startswith('td'):
        td_path = file
        td = td(td_path)
        td.clean_up()

        #testcases
        #pprint.pprint(td.fixed_date)
        #pprint.pprint(td.fixed_name)
        #pprint.pprint(td.fixed_transaction)
        #pprint.pprint(td.expenditure)
        #pprint.pprint(td.account)


print("Everything checks out chief")