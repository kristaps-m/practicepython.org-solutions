# Pick Word
# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html



import sys;
def randWord():
    import random;
    f = open("sowpods.txt");
    # ~ print(f.read()); # prints all words in console
    big_list = [i.split()[0] for i in f];
    RW = random.choice(big_list); # random word
    f.close();
    return [i for i in RW];
    # ~ print(len(big_list)); # Check lenght of list(words)





def hangMan():
    theWord = randWord(); #["P","I","M","P","I","S"]#"PIMPIS"#
    print("Welcome to Hangman! Here is your world...");
    L = ["_" for i in range(len(theWord))];
    print("  "+" ".join(L));
    output = [];
    NrWord = dict(enumerate(theWord));
    
    
    while True:
        UI = input(" Enter a letter: ").upper(); 
        # ~ A = 
        if UI in theWord and UI not in L:            
            for n, letter in NrWord.items():
                if letter == UI:
                    L[n] = letter.upper();
                    if L == theWord:
                        print(" Game over you won!!");
                        print(" The word is: {}".format("".join(L)));
                        sys.exit();
            print(" "+" ".join(L));
                # ~ #print(L,theWord);
        elif UI in L:
            print(" Already guesed that letter. It is in the Secret Word!");
            
        else:
            print(" Incorrect");   
    
    
print(hangMan())
