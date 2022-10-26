class Configuration:
    MONTH = 0
    DAY = 1
    YEAR = 2

class Checklist:
#Naming Change
    s_checklist = ["AMZN","FROM","UBER","LYFT","PRESTO","BERTO",
                "SONNET","TIM","MCDONALD","Amazon","VIRGIN",
                "ROSE","FRESHCO","PAT","DOLLARAMA","APPLE","Riot",
                "GOOGLE","Customer Transfer"]
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
                    "Transfer Scotia - Debit -> Scotia - Visa"
                    ]

    e_checklist = ["EAT","EATS"]

    e_replacements = ["UberEats - ",
                    "UberEats - "
                    ]