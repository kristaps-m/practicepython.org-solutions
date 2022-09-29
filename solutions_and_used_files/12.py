"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
 and makes a new list of only the first and last elements of the given list.
 For practice, write this code inside a function"""

a = [5, 10, 15, 20, 25,30,35,40,45,50,55,60,65,70];

def firstAndLast(X):
    newL = [value for number,value in enumerate(X) if number ==0 or number==len(X)-1];
    newL2 = [X[0],X[-1]];
    return newL;
    
print(firstAndLast(a));
