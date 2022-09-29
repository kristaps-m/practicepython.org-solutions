# Birthday Json
# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
import json;

# ~ birthdates = {"Britney Spears": "02.12.81", "Selena Gomez":"22.07.87", "Arnold Schwarzenegger":"30.07.47"};
# ~ with open("exercise 34 info.json", "r") as f:
    # ~ info = json.load(f)

# ~ print(info);
# ~ for k,v in info.items():
    # ~ print(k,v);


# ~ info_about_me = {
    # ~ "Nicole Scherzinger": "29.06.78",
    # ~ "Brad Pitt": "18.12.63"}

# ~ # update file!
# ~ with open("exercise 34 info.json", "r+") as f:
    # ~ data = json.load(f)
    # ~ data.update(info_about_me)
    # ~ f.seek(0)
    # ~ json.dump(data, f)

# ~ # open and print
# ~ with open("exercise 34 info.json", "r") as f:
    # ~ info = json.load(f)
# ~ print(info);

with open("exercise 34 info.json", "r") as f:
    info = json.load(f)

def birthDate(D):
    print("Welcome to the birthday dictionary. We know the birthdays of:\n");
    # ~ with open("exercise 34 info.json", "r") as f:
        # ~ info = json.load(f)
    for i in D.keys():
        print(i);
    
    while True:
        ask_user = input("Add B.D. or check B.D or All List. Enter 'add' or 'check' or 'alllist'. Here: ");
        if ask_user == "add":
            tempDict = {};
            FNandLN = input("Enter First Name and Last Name 'Brad Pitt' Here: ");
            Bdate = input("Enter birthday 'dd.mm.yy' Here: ");
            tempDict = {FNandLN:Bdate}
            print(f"{FNandLN} added with {Bdate}");
            # ~ updateDict(D,tempDict)
            with open("exercise 34 info.json", "r+") as f:
                data = json.load(f)
                data.update(tempDict)
                f.seek(0)
                json.dump(data, f)
            tempDict = {};
        elif ask_user == "check":
            with open("exercise 34 info.json", "r") as f:
                info = json.load(f);
            # ~ print(" ".join(i for i in info.keys()));
            print("\nWho's birthday do you want to look up?");
            UI = input(" Enter: ");
            print(f"{UI}'s birthday is {info[UI]}.");
        elif ask_user == "alllist":
            with open("exercise 34 info.json", "r") as f:
                info = json.load(f);
            for i in info.keys():
                print(i);
        else:
            print("Enter 'add' or 'check' please!");
            # ~ for i in D.keys():
                # ~ print(i);
    
    
def updateDict(the_file, update_dict):
    # update file!
    with open(the_file, "r+") as f:
        data = json.load(f)
        data.update(update_dict)
        f.seek(0)
        json.dump(data, f)
    return the_file;
    
birthDate(info);
