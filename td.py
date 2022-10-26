from config import Configuration, Checklist
import pandas as pd
import re
class td:
    def __init__(self, td_path):
        
        #Creating a dataframe out of the CSV file
        df = pd.read_csv(td_path,
                            names=['Date','Name','Out','In','Total'])

        #Creation of lists
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

            
            # cost = float(cost)
            # if cost < 0:
            #     cost = cost * -1
            #     cost = format(cost, '.2f')
            #     self.fixed_transaction.append(cost)
            #     self.expenditure.append("Out")
            # elif cost >= 0:
            #     cost = format(cost, '.2f')
            #     self.fixed_transaction.append(cost)
            #     self.expenditure.append("In")

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

            self.fixed_name.append(description)