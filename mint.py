from config import Date, Checklist
import pandas as pd
import re

# class for mint csv files
class mint:
    def __init__(self, mint_path):
        
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(mint_path)

        #Creation of variables and lists
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
        
    #Activates all fixes
    def clean_up(self):
        self.fix_date()
        self.fix_name()
        self.fix_transaction()

    #Fixes date format
    def fix_date(self):

        #Splits the date, makes them all 2 sig figs
        for entry in self.date:
            seperated = entry.split("/")
            if len(seperated[Date.MONTH]) == 1:
                fixed_m = '0' + seperated[Date.MONTH]
                seperated[Date.MONTH] = fixed_m
            if len(seperated[Date.DAY])== 1:
                fixed_d = '0' + seperated[Date.DAY]
                seperated[Date.DAY] = fixed_d
            if len(seperated[Date.YEAR]) == 4:
                fixed_y = seperated[Date.YEAR][2:]
                seperated[Date.YEAR] = fixed_y

            # Swaps position of month and day
            seperated[Date.MONTH], seperated[Date.DAY] = seperated[Date.DAY], seperated[Date.MONTH]
            entry = "-".join(seperated)
            # Inserts entry into front of fixed_date list -> Due to format of mint file
            self.fixed_date.insert(0, entry)
    
    #Fixes transaction format
    def fix_transaction(self):    
        
        # Produces list of the direction of money flow
        for i, expend in enumerate(self.ttype):
            x = re.search("^debit", expend)
            if x != None:
                self.expenditure.append("Out")
            else:
                self.expenditure.append("In")
        
        # Formats to 2 sig figs, inserts to front of list -> Due to format of mint file
        for cost in self.transaction:
            cost = format(cost, '.2f')
            self.fixed_transaction.insert(0, cost)

    #Fixing naming format
    def fix_name(self):
        
        for description in self.name:
            x = 0
            
            while x == 0:
                description = description.strip()
                for word in Checklist.r_checklist:
                    if description.endswith(word):
                        description = description.rstrip(word)
                        description = description.strip()
                    else:
                        x = 1
            
            #Checks for content existing in end checklist, replaces with replacement
            for i, word in enumerate(Checklist.e_checklist):
                if description.endswith(word):
                    description = Checklist.e_replacements[i]

            #Checks for content existing in start checklist, replaces with replacement
            for i, word in enumerate(Checklist.s_checklist):
                if description.startswith(word):
                    description = Checklist.s_replacements[i]
                    
            # Inserts entry into front of list -> Due to format of mint file
            self.fixed_name.insert(0, description)
