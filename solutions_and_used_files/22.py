# Read From File
#https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

from collections import Counter;
f= open("Read From File. ex 22.txt","r");
L = [i.split()[0] for i in f];
C = Counter(L);
print(C);
print(L);
# ~ print(f.read());























f.close();
