#!/usr/bin/env python3
import os
import pprint
import pandas as pd
import shutil
from scotia import scotia_visa, scotia_debit
from mint import mint
from td import td



def usage():
    print("This program will parse all csv files in the bank folder and output them to the banking_files folder.")
    print("The csv files must be named as follows: ")
    print("     Scotia_Visa_XXXXXX.csv")
    print("     Scotia_Debit_XXXXXX.csv")
    print("     transactions_XXXXXX.csv\n")
    print("Usage: python3 main.py <options>")
    print("Options:")
    print("     -h, --help: Display this message")
    print("     -f, --file: Specify a file to parse. Can be anywhere on the system. Ignoes bank folder.")
    exit(0)



#list of csvs inside the bank folder
csvs = []
OUTPUT = os.getcwd() + '/output'

#Open bank folder and grab all csv file names
def readFromBank():
    if not os.path.isdir('bank'):
        print("Bank folder not found. Creating bank folder.")
        os.mkdir('bank')
        exit(0)

    os.chdir('bank')
    csvFiles = os.listdir()

    for file in csvFiles:
        if file.endswith('.csv'):
            csvs.append(file)        


#matching file to their respective class     
def parse():
    for file in csvs:
        if 'Scotia_Visa' in file:
            visa = scotia_visa(file)
            visa.clean_up()
            visa_dict = {'Date': visa.fixed_date,
                        'Expenditure': visa.expenditure,
                        'Description': visa.fixed_name,
                        'Category': visa.category,
                        'Account': visa.account,
                        'Amount': visa.fixed_transaction}
            visa_df = pd.DataFrame(visa_dict)
            filename = os.path.split(file)[-1]
            visa_df.to_csv(f'{OUTPUT}/{filename[:-4]}_processed.csv', index = False)

        elif 'Scotia_Debit' in file:
            debit = scotia_debit(file)
            debit.clean_up()
            debit_dict = {'Date': debit.fixed_date,
                        'Expenditure': debit.expenditure,
                        'Description': debit.fixed_name,
                        'Category': debit.category,
                        'Account': debit.account,
                        'Amount': debit.fixed_transaction}
            debit_df = pd.DataFrame(debit_dict)
            filename = os.path.split(file)[-1]
            debit_df.to_csv(f'{OUTPUT}/{filename[:-4]}_processed.csv', index = False)
        
        elif 'transactions' in file:
            mint = mint(file)
            mint.clean_up()
            mint_dict = {'Date': mint.fixed_date,
                        'Expenditure': mint.expenditure,
                        'Description': mint.fixed_name,
                        'Category': mint.category,
                        'Account': mint.account,
                        'Amount': mint.fixed_transaction}
            mint_df = pd.DataFrame(mint_dict)
            filename = os.path.split(file)[-1]
            mint_df.to_csv(f'{OUTPUT}/{filename[:-4]}_processed.csv', index = False)
        
        elif 'td' in file:
            tdObj = td(file)
            tdObj.clean_up()
            td_dict = {'Date': tdObj.fixed_date,
                        'Expenditure': tdObj.expenditure,
                        'Description': tdObj.fixed_name,
                        'Category': tdObj.category,
                        'Account': tdObj.account,
                        'Amount': tdObj.fixed_transaction}
            td_df = pd.DataFrame(td_dict)
            filename = os.path.split(file)[-1]
            td_df.to_csv(f'{OUTPUT}/{filename[:-4]}_processed.csv', index = False)


    print("Everything checks out chief, Files processed")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file', type=argparse.FileType('r'), help='input CSV file')
    parser.add_argument('-ch', '--custom-help',  action='store_true', help='show custom help message')
    args = parser.parse_args()

    if args.custom_help:
        usage()

    if not os.path.isdir('output'):
        os.mkdir('output')

    if args.file:
        csvs.append(args.file.name)
        parse()

    else:
        readFromBank()
        parse()
