#Cow and Bulls
#https://en.wikipedia.org/wiki/Bulls_and_Cows
from random import randint;
# random 4 dig Nr, No duplicates, first can be 0, returns str()
def getRandomNum(X):     
    S = "";
    while True:
        random_n = str(randint(0,9));
        if random_n not in S:
            S+=random_n;
        if len(S)==X: #"""Can we change it?"""
            break;
    return S;

#Game logic?! Bulls and Cows count
def bullsAndCows(num, userInput):
    bulls = 0;
    cows = 0;
    for n,u in zip(num,userInput):
        if n==u:
            bulls+=1;
        elif u in num and u != n:
            cows += 1;
    return bulls,cows;
#Makes sure user uses only digits
def allDigits(userCheats):
    return all(1 if i in "0123456789" else 0 for i in userCheats);
        


# ~ print(theOneRandNum);

# 1234 == 1297 ## 9012

def theGame():    
    print("Welcome to Cows and Buls! Type: 'exit' to leave game :(");
    print("If the matching digits are in their right positions, they are \"bulls\", if in different positions, they are \"cows\".")
    AMOUT = int(input("How big the secret Nr will be?: 1-9? Please enter 4 :)"));
    print("Try to gues the number!");
    theOneRandNum = getRandomNum(AMOUT); #The random number variable;
    game_cout = 1;
    while True and game_cout<999999:
        UI = input("  Enter here:  ");
        if UI == "exit":
            print(f"Bye! Next time don't give up! Nr = {theOneRandNum}");
            print(f"You LOST! You tryed to guess {game_cout} times!");
            break;
        elif len(UI) != AMOUT: #"""Can we change it?"""#
            print(f"Please enter {AMOUT} digit number!!!");
        elif not allDigits(UI):
            print("Please enter only digits! +1 Atempt for u!");
        elif len(set(UI)) != AMOUT: #"""Can we change it?"""#
            print("Don't use duplicates!");
        elif UI == theOneRandNum:
            print(f"You won! You tryed to gues {game_cout} times!");
            break;
        else:        
            print(f"    Wrong number! Bulls: {bullsAndCows(theOneRandNum, UI)[0]},\
     Cows: {bullsAndCows(theOneRandNum, UI)[1]}");        
            game_cout += 1;


if __name__=="__main__":
    theGame()
