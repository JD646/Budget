from config import Date, Checklist




def clean(description, word):
    x = 0
    description = description.strip()
    print("Strip outside of if - " + description)
    while x == 00:
        if description.endswith(word):
            description = description.rstrip(word)
            print("Rstrip word - " + description)
            description = description.rstrip()
            print("Rstrip - " + description)
        else:
            print("completed w phrase - " + description)
            x = 1

def old_clean(description, word):
    x = 0
    while x == 0:
        description = description.strip()
        print("Strip outside of if - " + description)
        for word in Checklist.r_checklist:
            if description.endswith(word):
                description = description.rstrip(word)
                print("Rstrip word - " + description)
                description = description.strip()
                print("Rstrip - " + description)
            else:
                print("completed w phrase - " + description)
                x = 1

a = "THIRSTEA MISSISSAUGA     MISSISSAUGA  "


clean(a, "MISSISSAUGA")
print("VS")
#old_clean(a)

