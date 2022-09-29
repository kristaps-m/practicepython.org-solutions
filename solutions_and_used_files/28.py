# Max Of Three
# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

def maxoftree():
    print("Welcome to max of tree game!");
    print("Exaple: 1 123 6753. Devide numbers with space");
    UI = input("Please enter 3 numbers and I will tell you biggest number: ");
    
    a = int(UI.split()[0]);
    b = int(UI.split()[1]);
    c = int(UI.split()[2]);
    
    if a > b and a > c:
        return a;
    elif b > c:
        return b;
    else:
        return c;
        
C = 10000;
while C > 0:      
    print(maxoftree());
    C = C - 1;
