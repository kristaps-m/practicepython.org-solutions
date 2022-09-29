# Hangman
# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

from sys import exit;
from time import sleep;
def randWord():
    import random;
    f = open("sowpods.txt");
    # ~ print(f.read()); # prints all words in console
    big_list = [i.split()[0] for i in f];
    RW = random.choice(big_list); # random word
    f.close();
    return [i for i in RW];
    # ~ print(len(big_list)); # Check lenght of list(words)


def picture(lives):
    Graphics=['''
------------
|         |
|        
|        
|         
|           
|___________________
 ''','''
------------
|         |         
|         O
|       
|        
|         
|___________________
 ''',
 '''
------------
|         | 
|         O 
|        / 
|          
|          
|___________________
 ''',
 '''
------------
|         | 
|         O 
|        / \\
|          
|          
|___________________
 ''','''
------------
|         | 
|         O 
|        / \\ 
|         |
|           
|___________________
 ''','''
------------
|         |
|         O 
|        / \\
|         |
|        /  
|___________________
            ''',
'''
------------
|         |
|         O 
|        / \\
|         |
|        / \\ 
|___________________
            '''            ]
    return Graphics[lives];


def hangMan(X):
    theWord = randWord(); #["P","I","M","P","I","S"]#"PIMPIS"#
    # ~ theWord = ["P","I","M","P","I","S"];
    L = ["_" for i in range(len(theWord))];
    print("\n Welcome to Hangman! Here is your world...");
    print("  "+" ".join(L));
    print(" You have 6 lives!")#, (f"CHEAT = {theWord}");  
    print(picture(0));
    output = [];
    NrWord = dict(enumerate(theWord));
    guesses_cout = X;
    guesses_set = set();
    
    
    while guesses_cout > -1:
        print(f"Set of used letters {'{}' if len(guesses_set)==0 else guesses_set}. Progress of word: {' '.join(L)}");
        UI = input(" Enter a letter: ").upper(); 

        # ~ A = 
        if UI in theWord and UI not in L:
            for n, letter in NrWord.items():
                if letter == UI:
                    L[n] = letter.upper();
                    guesses_set.add(UI);
                    if L == theWord:
                        print(" Game over you won!!");
                        print(" The word is: {}".format("".join(L)));
                        # ~ exit();
                        sleep(1);
                        for i in range(20):
                            print();
                            sleep(0.15);
                        newGame()
            print(" "+" ".join(L));
                # ~ #print(L,theWord);
        elif UI in L:
            print(" Already guesed that letter. It is in the Secret Word!");
            print(" "+" ".join(L));
            
        else:
            if UI not in guesses_set and UI not in theWord and UI not in L and len(UI)==1:
                guesses_cout -= 1; # It maters where you put this
                # Before or after you print lives left
                if guesses_cout == 0:
                    print("Game Over! You have 0 lives left");
                    print(picture(6-guesses_cout));
                    print(" The word was: "+" ".join(theWord));
                    # ~ exit();
                    sleep(1);
                    for i in range(20):
                        print();
                        sleep(0.15);
                    newGame()
                else:
                    print(" Incorrect", f"You have {guesses_cout} lives left"); 
                    print(picture(6-guesses_cout));
                    guesses_set.add(UI);

            else:
                # ~ guesses_set.add(UI);
                print(" Incorrect! :( ", f"Set of used letters {guesses_set}"); 
    
    
    
def newGame():
    # ~ print("XXXXXXXXX Welcome to Hangman! Here is your world...");
    hangMan(6)
    
    
# ~ print(hangMan())
newGame()
