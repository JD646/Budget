from config import Date, Checklist
import pandas as pd

#Class for TD Debit
class td:
    def __init__(self, td_path):
        
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(td_path,
                            names=['Date','Name','Out','In','Total'])

        #Creation of variables and lists
        date = df['Date'].values.tolist()
        name = df['Name'].values.tolist()
        spend = df['Out'].values.tolist()
        save = df['In'].values.tolist()
        self.spend = spend
        self.save = save
        self.date = date
        self.name = name
        self.fixed_date = []
        self.fixed_name =[]
        self.fixed_transaction = []
        self.expenditure = []
        self.account = []
        self.category = []
        
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
            # Labels which account it came from
            self.account.append("TD - All Inclusive")
    
    #Fixes transaction format
    def fix_transaction(self):    
        #Compiles data from money out and money in into fixed_transaction list, Produces list of direction of money flow
        for i, cost in enumerate(self.spend):
            cost = str(cost)
            if "nan" in cost:
                cost = float(cost)
                cash = format(self.save[i], '.2f')
                self.fixed_transaction.append(cash)
                self.expenditure.append("In")
            else:
                cost = float(cost)
                cost = format(cost, '.2f')
                self.fixed_transaction.append(cost)
                self.expenditure.append("Out")

    #Fixes naming format
    def fix_name(self):
        
        for x, description in enumerate(self.name):
            separated = description.split()
            self.category.append('Jonas')
            
            # Checks for words on remove list, adds words not found in remove list into [corrected] to replace original phrase
            corrected = []
            for word in separated:
                if word not in Checklist.r_checklist:
                    corrected.append(word)
            description = " ".join(corrected)
            
            #Checks for content existing in end checklist, replaces with replacement
            for i, word in enumerate(Checklist.e_checklist):
                if description.endswith(word):
                    description = Checklist.e_replacements[i]
                    self.category[x] = Checklist.e_category[i]

            #Checks for content existing in start checklist, replaces with replacement
            for i, word in enumerate(Checklist.s_checklist):
                if description.startswith(word):
                    description = Checklist.s_replacements[i]
                    self.category[x] = Checklist.s_category[i]

            #Insert into fixed_name list
            self.fixed_name.append(description)