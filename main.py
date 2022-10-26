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
    if '.csv' in file:
        csvs.append(file)        

#matching file to their respective class       
for file in csvs:
    if 'Scotia_Visa' in file:
        visa_path = file
        visa = scotia_visa(visa_path)
        visa.clean_up()

        #testcases
        #pprint.pprint(visa.fixed_date)
        #pprint.pprint(visa.fixed_name)
        #pprint.pprint(visa.fixed_transaction)
        #pprint.pprint(visa.expenditure)

    elif "Scotia_Debit" in file:
        debit_path = file
        debit = scotia_debit(debit_path)
        debit.clean_up()

        #testcases
        #pprint.pprint(debit.fixed_date)
        #pprint.pprint(debit.fixed_name)
        #pprint.pprint(debit.fixed_transaction)
        #pprint.pprint(debit.expenditure)
    
    elif "transactions" in file:
        mint_path = file
        mint = mint(mint_path)
        mint.clean_up()

        #testcases
        #pprint.pprint(mint.fixed_date)
        #pprint.pprint(mint.fixed_name)
        #pprint.pprint(mint.fixed_transaction)
        #pprint.pprint(mint.expenditure)
    
    elif "td" in file:
        td_path = file
        td = td(td_path)
        td.clean_up()

        #testcases
        #pprint.pprint(td.fixed_date)
        #pprint.pprint(td.fixed_name)
        #pprint.pprint(td.fixed_transaction)
        #pprint.pprint(td.expenditure)

print("Everything checks out chief")