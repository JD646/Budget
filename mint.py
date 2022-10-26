from config import Configuration, Checklist
import pandas as pd
import re

class mint:
    def __init__(self, mint_path):
        
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(mint_path)

        #Creation of lists
        date = df['Date'].values.tolist()
        name = df['Description'].values.tolist()
        transaction = df['Amount'].values.tolist()
        ttype = df['Transaction Type'].values.tolist()
        account = df['Account Name'].values.tolist()
        label = df['Labels'].values.tolist()
        self.date = date
        self.name = name
        self.transaction = transaction
        self.ttype = ttype
        self.account = account
        self.label = label
        self.fixed_date = []
        self.fixed_name = []
        self.fixed_transaction = []
        self.expenditure = []
        
    ##FIXING OVERALL LIST FORMAT
    def clean_up(self):
        self.fix_date()
        self.fix_name()
        self.fix_transaction()

    #Fixing date format
    def fix_date(self):

        for entry in self.date:
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
            entry = "-".join(seperated)
            self.fixed_date.insert(0, entry)
    
    #Fixing transaction format
    def fix_transaction(self):    
        
        for i, expend in enumerate(self.ttype):
            x = re.search("^debit", expend)
            if x != None:
                self.expenditure.append("Out")
            else:
                self.expenditure.append("In")
        
        for cost in self.transaction:
            cost = format(cost, '.2f')
            self.fixed_transaction.insert(0, cost)

    #Fixing naming format
    def fix_name(self):
        

        for description in self.name:
            description = description.strip()
            
            description = description.rstrip("(GOOGLE PAY)")
            description = description.rstrip("(APPLE PAY)")
            description = description.rstrip()

            description = description.rstrip("ON")
            description = description.rstrip("BC")
            description = description.rstrip("AB")
            description = description.rstrip("QC")
            description = description.rstrip()

            description = description.rstrip("MISSISSAUGA")
            description = description.rstrip("Mississauga")
            description = description.rstrip("TORONTO")
            description = description.rstrip("ETOBICOKE")
            description = description.rstrip("VANCOUVER")
            description = description.rstrip("VERDUN")
            description = description.rstrip("CONCORD")
            description = description.rstrip("VAUGHAN")
            description = description.rstrip("WATERLOO")
            description = description.rstrip("HAMILTON")
            description = description.rstrip("OAKVILLE")
            description = description.rstrip()

            description = description.rstrip("866-712-7753")
            description = description.rstrip("C02404")
            description = description.rstrip("C02404")
            description = description.rstrip("#9685")
            description = description.rstrip()

            for i, item in enumerate(Checklist.e_checklist):
                x = re.search(item + "$" , description)
                if x != None:
                    description = Checklist.e_replacements[i]

            for i, item in enumerate(Checklist.s_checklist):
                x = re.search("^" + item, description)
                if x != None:
                    description = Checklist.s_replacements[i]

            self.fixed_name.insert(0, description)