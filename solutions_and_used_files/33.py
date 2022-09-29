# Birthday Dictionaries
# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

birthdates = {"Britney Spears": "02.12.81", "Selena Gomez":"22.07.87", "Arnold Schwarzenegger":"30.07.47"};

def birthDate(D):
    print("Welcome to the birthday dictionary. We know the birthdays of:\n");
    for i in D.keys():
        print(i);
    print("Who's birthday do you want to look up?");
    UI = input(" Enter: ");
    print(f"{UI}'s birthday is {D[UI]}.");
    
birthDate(birthdates);
