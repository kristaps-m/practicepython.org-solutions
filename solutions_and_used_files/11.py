UI = int(input("Hi! Give me number and i will tell you it it's prime or not! "));
def isPrime(X):
    if X<=1:
        return False
    C=0;
    n = 1;
    while n<X+1:
        if X % n ==0:         
            C+=1;
            n+=1;
        else:
            n+=1;
        if C>2:
            return False;
    return True;


if isPrime(UI):
    print(f"{UI} is Prime my friend");
else:
    print(f"{UI} is NOT prime my friend");



