# Tic Tac Toe Draw
# https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

game = [["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]

print("  Welcome to tic-tac-toe");
print("  We will make turns to enter X or O");
print("  Enter X or O in format 'row','col' exaple 3,2");
print("  Enter '1,1' as minimu value and '3,3' as maximum!");
print("  This is how the game board looks for now:");
for i in game:
    print(i);

def theGame(): # user_input
    game_count = 1;
    while True:
        PLNr = 1 if game_count % 2 == 1 else 2;
        # ~ print(game_count, PLNr);
        UI = input(f"Payer {PLNr} please enter 'row','col': ");
        # ~ print(UI)
        row = int(UI.split(",")[0]);
        col = int(UI.split(",")[1]);
        # ~ print(row,col);
        if game[row-1][col-1] == "X" or game[row-1][col-1] == "O":
            print("This sqare is already taken!");
        else:
            game[row-1][col-1] = "X" if game_count % 2 == 1 else "O";
        # X or O
            for i in game:
                print(i);
            game_count += 1;
            if game_count == 10:
                print("    Game over!");
                print("    And the Winer is .....!");
                break;

        
theGame()

# (in the format row,col)
