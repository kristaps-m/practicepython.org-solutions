import re;
# Read From File
#https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

from collections import Counter;
f= open("Training_01.txt","r");
# ~ print(f.read())

pattern = re.compile(r"(/\w/)([/\w+/]+)(sun_)");
x = re.findall(pattern,f.read())
#" ".join(x)
L= [i[1] for i in x]
# ~ print(L);
# ~ print(x);
C = Counter(L);
# ~ print(C);

"""The answer printed in lines"""
print();
for k,v in C.items():
    print(k,"=",v);










f.close();
