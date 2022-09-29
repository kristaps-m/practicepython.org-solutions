print("Welcome to  two-player Rock-Paper-Scissors game!");
print("Rock = R, Paper = P, Scissors = S");
# RP, RS, PR, PS, SR, SP 
SP1 = 0;
SP2 = 0;
while True:
    P1 = input("Player one ...").upper();
    P2 = input("Player two ...").upper();

    combo = P1+P2;
    D = ["RS", "PR","SP"];
    if P1 == P2:
        print("Tie");
    elif combo in D:
        print("Player one have won");
        SP1 +=1;
    else:
        print("Player TWO have won");
        SP2 += 2;
    print("Player 1 = {}  ||   Player 2 = {}".format(SP1,SP2));
