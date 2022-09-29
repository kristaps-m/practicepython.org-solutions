#List Remove Duplicates
from random import randint;
theList = [randint(0,50) for i in range(100)];
print(f"The original list length {len(theList)}");
newList = sorted(set(theList))
print(newList);
print();
print(f"New list len with out duplicates = {len(newList)}");

def loopDupl(X):
    L=[]
    for i in X:
        if i not in L:
            L.append(i);
    return sorted(L);
    
print(loopDupl(theList));
