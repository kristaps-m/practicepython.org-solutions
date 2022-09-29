# Fibonacci

def Fib(X):
    seq = [1,1];
    for i in range(X-2):
        seq.append(seq[-1]+seq[-2]);
    return "There u go:  " + str(seq)[1:-1];
   
    
UI = int(input("Hello how many Fibonacci number you want to see?: "));

print(Fib(UI));

