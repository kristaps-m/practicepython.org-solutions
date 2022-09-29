# Tic Tac Toe Game
# https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
from sys import exit;
"""
Draw A Game Board
checking whether someone has WON a game
Handle a player move from user input
"""
""" 26 """
results_count = [];

def whoWon(X):
    L = [row(X),col(X),diag(X),diag2(X)]; # ?
    if L.count(None) == 4:
        return "Tie or Friendship! <3";
    elif L.count("P1") >= 1:
        return "Player '-1-' or 'X'";
    else:
        return "Player '-2-' or 'O'";
    
def row(X):
    for i in X:
        if i.count(1) ==len(X):
            return "P1";
        elif i.count(2)==len(X):
            return "P2";
def col(X):
    Big = []
    for i in range(len(X)):
        L= []
        for u in range(len(X)):
            L.append(X[u][i]);
        Big.append(L);
        L=[];
        
    for i in Big:
        if i.count(1) ==len(X):
            return "P1";
        elif i.count(2)==len(X):
            return "P2";            
            
def diag(X):
    Big = []
    for u in range(len(X)):
        Big.append(X[u][u]);   
    if Big.count(1) ==len(X):
        return "P1";
    elif Big.count(2)==len(X):
        return "P2";
        
        
def diag2(X):
    Big = []

    for u in range(len(X)):
        Big.append(X[u][len(X)-1-u]);        

    if Big.count(1) ==len(X):
        return "P1";
    elif Big.count(2)==len(X):
        return "P2";

"""---------------------------------"""



def drawBoard(X):
    R = [];
    
    # ~ R2 = ["|"];
    for i in range(1,X+1):
        R.append("---");
    rows = " "+" ".join(R);
    rows2 = [["|"]+["  |" for i in range(X)] for i in range(X)]
    result = "";
    for i in range(X):
        result += rows + "\n";
        result += " ".join(rows2[i]) + "\n";    
    
    #-----------Back end!
    BEB = [[0 for i in range(X)] for i in range(X)] #back end board
    # ~ for i in BEB: #print back end board
        # ~ print(i);

#---------------------------------------------------------------

    game = result + rows

    print("  Welcome to tic-tac-toe");
    print("  We will make turns to enter X or O");
    print("  Enter X or O in format 'row','col' exaple 3,2");
    print(f"  Enter '1,1' as minimu value and '{X},{X}' as maximum!");
    print("  This is how the game board looks for now:");
    print(game);

    game_count = 1;
    while True:
        PLNr = 1 if game_count % 2 == 1 else 2;
        # ~ print(game_count, PLNr);
        UI = input(f"Payer {PLNr} please enter 'row','col': ");
        row = int(UI.split(",")[0]);
        col = int(UI.split(",")[1]);
        # ~ print(row,col);
        if rows2[row-1][col] == "X |" or rows2[row-1][col] == "O |":
            print("This sqare is already taken!");
        else:
            rows2[row-1][col] = "X |" if game_count % 2 == 1 else "O |";
            BEB[row-1][col-1] = 1 if game_count % 2 == 1 else 2;
            result = "";
            for i in range(X):
                result += rows + "\n";
                result += " ".join(rows2[i]) + "\n";
            game = result + rows
            print(game);
            # ~ print(BEB); # Test Back end Board
            # ~ print(whoWon(BEB)); # Test WhoWon output!
            game_count += 1;
            if game_count < X**2 + 1 and whoWon(BEB) == "Player '-1-' or 'X'" or game_count < X**2 + 1 and whoWon(BEB) == "Player '-2-' or 'O'":
                print("    Game over!");
                print(f"    And the Winer is {whoWon(BEB)} !");
                results_count.append(whoWon(BEB));
                # ~ break;
                theGameStart()
            elif game_count == X**2 + 1:
                print("    Game over!");
                print(f"    And the Winer is {whoWon(BEB)} !");
                results_count.append(whoWon(BEB));
                # ~ break;
                theGameStart()

      
# ~ theGame()
# ~ drawBoard(start_UI);


def theGameStart():
    UI2 = input("Enter option: 'Start', 'Quit': ");
    if UI2 == "Start":
        start_UI = int(input("How big board do you want?: "));
        drawBoard(start_UI);
    elif UI2 == "Quit":
        print("Good bye!");
        print("Player ONE= {}".format(results_count.count("Player '-1-' or 'X'"))); 
        print("Player TWO= {}".format(results_count.count("Player '-2-' or 'O'")));
        exit(); # sys.exit()
        
        # ~ results_count = [];
        # ~ drawBoard(X)
        # ~ break;
    # ~ while True:
        # ~ drawBoard(start_UI);


theGameStart()
