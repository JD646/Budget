from config import Configuration
import pandas as pd
class scotia_visa:
    def __init__(self, visa_path):
        
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(visa_path,
                            names=['Date','Name','Transaction'])

        #Creation of lists
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
            self.fixed_date.append(entry)
    
    #Fixing transaction format
    def fix_transaction(self):    

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

    #Fixing naming format
    def fix_name(self):

        for description in self.name:
            description = description.strip()
            
            description = description.rstrip("(GOOGLE PAY)")

            description = description.rstrip("ON")
            description = description.rstrip("BC")
            description = description.rstrip("AB")
            description = description.rstrip()

            description = description.rstrip("MISSISSAUGA")
            description = description.rstrip("TORONTO")
            description = description.rstrip("ETOBICOKE")
            description = description.rstrip("VANCOUVER")
            description = description.rstrip()
            
            self.fixed_name.append(description)


class scotia_debit:
    def __init__(self, debit_path):
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(debit_path,
                            names=['Date','Name','Transaction'])

        #Creation of lists
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
            self.fixed_date.append(entry)


    
    #Fixing transaction format
    def fix_transaction(self):    

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


    #Fixing naming format
    def fix_name(self):

        for description in self.name:
            description = description.strip()
            
            description = description.rstrip("(GOOGLE PAY)")

            description = description.rstrip("ON")
            description = description.rstrip("BC")
            description = description.rstrip("AB")
            description = description.rstrip()

            description = description.rstrip("MISSISSAUGA")
            description = description.rstrip("TORONTO")
            description = description.rstrip("ETOBICOKE")
            description = description.rstrip("VANCOUVER")
            description = description.rstrip()
            
            self.fixed_name.append(description)