# Pick Word
# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html


import random;
f = open("sowpods.txt");
# ~ print(f.read()); # prints all words in console
big_list = [i.split()[0] for i in f];
RW = random.choice(big_list); # random word
print(RW);
# ~ print(len(big_list)); # Check lenght of list(words)






f.close();
