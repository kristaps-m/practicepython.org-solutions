# Draw A Game Board 
# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

def drawBoard(X):
    R = [];
    R2 = ["|"];
    for i in range(1,X+1):
        R.append("---");
    for i in range(1,X+1):
        R2.append("  |");
        
    rows = " "+" ".join(R);
    rows2 = " ".join(R2)
    result = rows + "\n" + rows2
    return (result + "\n") * X  + rows;
    
    
    
    
UI = int(input("How big board do you want?: "))
print(drawBoard(UI));
