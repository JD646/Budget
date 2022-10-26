# Class to sort date format
class Date:
    MONTH = 0
    DAY = 1
    YEAR = 2

# Class to filter through entries, replace known ones
class Checklist:
    #Start checklist
    s_checklist = ["AMZN","FROM","UBER","LYFT","PRESTO","BERTO",
                "SONNET","TIM","MCDONALD","Amazon","VIRGIN",
                "ROSE","FRESHCO","PAT","DOLLARAMA","APPLE","Riot",
                "GOOGLE","Customer Transfer","PCC","SEND","E-TRANSFER"]
    #Start replacements
    s_replacements = ["AMZN - ",
                    "Transfer Scotia - Debit -> Scotia - Visa",
                    "Uber - ",
                    "Lyft - ",
                    "Presto Fare",
                    "Berto's",
                    "Sonnet Home Insurance",
                    "Tim Hortons",
                    "McDonalds",
                    "AMZN - ",
                    "Virgin Mobile - Internet and Phone",
                    "Rose Bakery",
                    "FreshCo",
                    "PAT Supermarket",
                    "Dollarama",
                    "ICloud Subscription",
                    "Riot Points",
                    "GDrive Subscription",
                    "Transfer Scotia - Debit -> Scotia - Visa",
                    "Home Management Fee",
                    "ETrans to - ",
                    "ETrans from -"
                    ]
    
    #End checklist
    e_checklist = ["EAT","EATS"]
    #End replacements
    e_replacements = ["UberEats - ",
                    "UberEats - "
                    ]

    #Remove checklist
    r_checklist = [""]