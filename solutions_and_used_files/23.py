#File Overlap
# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

happy = open("happynumbers.txt","r");
prime = open("primenumbers.txt","r");

H = [i.split() for i in happy];
P = [i.split() for i in prime]

result = [];
for i in H:
    # ~ print(i);
    if i in P:
        result.append(i[0]);
        
print(result);
















happy.close();
prime.close();
