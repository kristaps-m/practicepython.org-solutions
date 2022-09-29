from random import randint;
a = randint(1,9);
print(a, type(a));

print("Welcome to guesing game.\nGues number from 1 to 9.");
print("Type 'exit' to exit the game :)");
gueses = 1;

while True:
    UI = input("Please enter number: ")
    if UI == "exit":
        print("Please come back!");
        break;

    elif int(UI) == a:
        print(f"You have guesed the number. It is {a}!\nYou guesed in {gueses} times!");
        break;
        
    elif int(UI) > a:
        print("Number is lower!");
        gueses+=1;
    else:
        print("Number is higher!");
        gueses+=1;
        
