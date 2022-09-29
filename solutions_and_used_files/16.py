import string;
import random;
A = string.ascii_letters + "!@#$%^&*()~?<>" + string.digits;
#print(random.choice(A));


def PW(X):
    S = "";
    for i in range(X):
        S+= random.choice(A);
    return S;

while True:
    UI = int(input("How long you want your strong PW?:  "));    
    print(PW(UI));
