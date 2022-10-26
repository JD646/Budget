from config import Date, Checklist
import pandas as pd
import re
# Class for scotia visa
class scotia_visa:
    def __init__(self, visa_path):
        
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(visa_path,
                            names=['Date','Name','Transaction'])

        #Creation of variables and lists
        date = df['Date'].values.tolist()
        name = df['Name'].values.tolist()
        transaction = df['Transaction'].values.tolist()
        self.date = date
        self.transaction = transaction
        self.name = name
        self.fixed_date = []
        self.fixed_name =[]
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

            # Inserts entry into fixed_date list
            self.fixed_date.append(entry)
    
    #Fixes transaction format
    def fix_transaction(self):    

        # Produces list of the direction of money flow, formats to 2 sig figs, adds to fixed_transaction list
        for cost in self.transaction:
            cost = float(cost)
            if cost < 0:
                cost = cost * -1
                cost = format(cost, '.2f')
                self.fixed_transaction.append(cost)
                self.expenditure.append("Out")
            elif cost >= 0:
                cost = format(cost, '.2f')
                self.fixed_transaction.append(cost)
                self.expenditure.append("In")

    #Fixes naming format
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

            #Insert into fixed_name list
            self.fixed_name.append(description)

###-----------------------------------------------------------------

# Class for scotia debit
class scotia_debit:
    def __init__(self, debit_path):
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(debit_path,
                            names=['Date','Transaction','nada1','Name','nada2'])

        #Creation of variables and lists
        date = df['Date'].values.tolist()
        name = df['Name'].values.tolist()
        transaction = df['Transaction'].values.tolist()
        self.date = date
        self.transaction = transaction
        self.name = name
        self.fixed_date = []
        self.fixed_name =[]
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

            # Inserts entry into fixed_date list
            self.fixed_date.append(entry)


    
    #Fixes transaction format
    def fix_transaction(self):    

        # Produces list of the direction of money flow, formats to 2 sig figs, adds to fixed_transaction list
        for cost in self.transaction:
            cost = float(cost)
            if cost < 0:
                cost = cost * -1
                cost = format(cost, '.2f')
                self.fixed_transaction.append(cost)
                self.expenditure.append("Out")
            elif cost >= 0:
                cost = format(cost, '.2f')
                self.fixed_transaction.append(cost)
                self.expenditure.append("In")


    #Fixes naming format
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
            #Insert into fixed_name list
            self.fixed_name.append(description)