# Check Tic Tac Toe
# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

def whoWon(X):
    L = [row(X),col(X),diag(X),diag2(X)]; # ?
    # ~ player_one = [];
    # ~ player_two = [];
    # ~ for i in range(len(X)):
        # ~ for u in range(len(X)):
            # ~ pass
    if L.count(None) == 4:
        return "Tie";
    elif L.count("P1") >= 1:
        return "P1";
    else:
        return "P2";
    # ~ return L;
    
def row(X):
    # ~ while 
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
    # ~ return Big;
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
    # ~ return Big;
# ~ #def rowWon(X):
    # ~ L = [];
    # ~ for i in range(len(X)):
        # ~ for u in range(len(X)):
            # ~ L.append(X[i][u]);
            # ~ if list(set(L))[0]==2 and len(L) ==3:
                # ~ player_two.append(1);
            # ~ elif list(set(L))[0]==1 and len(L) ==3:
                # ~ player_one.append(1);
            # ~ elif list(set(L))[0] != 2 and len(L) <3:
                # ~ player_one.append(0);
            # ~ elif list(set(L))[0] != 1 and len(L) <3:
                # ~ player_one.append(0);
                
                
        # ~ L = [];


# ~ #def columnWon(X):
    # ~ L = [];
    # ~ for i in range(len(X)):
        # ~ for u in range(len(X)):
            # ~ L.append(X[u][i]);
            # ~ print(L)
            # ~ if list(set(L))[0]==2 and len(L) ==3:
                # ~ player_two.append(1);
            # ~ elif list(set(L))[0]==1 and len(L) ==3:
                # ~ player_one.append(1);
            # ~ elif list(set(L))[0] != 2 and len(L) <3:
                # ~ player_one.append(0);
            # ~ elif list(set(L))[0] != 1 and len(L) <3:
                # ~ player_one.append(0);
        # ~ L = [];
    # ~ print(player_one, player_two);
    
winner_is_2 = [[2, 2, 0],
                [2, 1, 0],
                [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
                [2, 1, 0],
                [2, 1, 1]]

winner_is_also_1 = [[0, 2, 0],
                    [2, 2, 0],
                    [2, 2, 1]]

no_winner = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                [2, 1, 0],
                [2, 1, 0]]
                
winner_is_1b = [[2, 0, 0],
                [2, 0, 2],
                [2, 1, 1]]
    
diagonal = [[0, 1, 2],
            [1, 2, 0],
            [2, 1, 0]]
    
Test22 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    
Test33 = [[2, 1, 2],
        [2, 1, 2],
        [2, 2, 2]]
    
mega_test = [[0,0,0,0,0,0,0,2],
            [0,0,0,0,0,0,2,0],
            [1,0,0,0,0,2,0,0],
            [1,0,0,0,2,0,0,0],
            [1,0,0,2,0,0,0,0],
            [1,0,2,0,0,0,0,0],
            [1,2,0,0,0,0,0,0],
            [2,0,0,0,0,0,0,0]]
    
print(whoWon(winner_is_2));
print(whoWon(winner_is_1));
print(whoWon(winner_is_also_1));
print(whoWon(no_winner));
print(whoWon(also_no_winner));
print(whoWon(winner_is_1b));
print(whoWon(diagonal));
print(whoWon(Test22));
print(whoWon(Test33));
print();
print(whoWon(mega_test));






