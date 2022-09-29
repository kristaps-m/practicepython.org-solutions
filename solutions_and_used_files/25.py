# Guessing Game Two
# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
'''0'''
'''UI = high, low, mynumber'''
# Here starts Binary search        
def midIndx(X): # Gets mid index for all time!
    res = int(len(X) // 2);
    return res;

def binarySearch(List,nr_pc_2_guess):
    bin_search_steps = 1; # Counts how many time List is split in half before result is found
    mid_number = List[midIndx(List)]; # Number in ~middle of List
    print("User say something about number i guesed. 'high','low' or 'mynumber'")
    
    # List 
    while True:
        # ~ print(List);
        print(f"Hi, user is your number: {mid_number} ?");
        user_answers = input(f"Is your Nr: {mid_number} ? Type: 'high','low' or 'mynumber' ? ")
        if nr_pc_2_guess == mid_number and user_answers == 'mynumber':
            return f"YES user i found {UI}. It's in the List [0-{len(L)-1}]. It took {bin_search_steps} Binary Search steps!"
            break;
        elif len(List)==1:
            if nr_pc_2_guess not in List:
                return f" Sorry {UI} is not in the List.\n Or You made mistake somewhere.\n It took {bin_search_steps} Binary Search steps!"; 
                """You can add 'nr_pc_2_guess < mid_number and' & 'nr_pc_2_guess < mid_number and' So you don't make mistake. 
                Like if your Nr is 10, PC gueses 50 and you say 'high'"""
        elif user_answers == 'low': #  nr_pc_2_guess < mid_number and 
            List = List[:midIndx(List)];
            mid_number = List[midIndx(List)];
        elif user_answers == 'high': # nr_pc_2_guess > mid_number and 
            List = List[midIndx(List):];
            mid_number = List[midIndx(List)];   
        bin_search_steps += 1;
"""List [0-100]"""
L = [i for i in range(0,101)]; #Make bigger list here...

"""Optional checks, List, Len, midle index"""
# ~ print(f"Len of list = {len(L)}");
# ~ print(f"The List ==...\n{L}");
# ~ print(f" mid Indx {midIndx(L)}");

"""Call Binary seach function"""
UI = int(input(f"We will make computer guess. Select Nr [0-{len(L)-1}] !  ")); 
print(binarySearch(L,UI));

