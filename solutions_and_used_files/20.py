# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
# Element Search

# Function with our Binary search
def inside(List, user_input):
    if user_input in List:
        return True;
    else:
        return False;
 
# Here starts Binary search        
def midIndx(X): # Gets mid index for all time!
    res = int(len(X) // 2);
    return res;

def binarySearch(List,user_input):
    bin_search_steps = 1; # Counts how many time List is split in half before result is found
    mid_number = List[midIndx(List)]; # Number in ~middle of List
    # List 
    while True:
        # ~ print(List);
        if user_input == mid_number:
            return f"YES you found {UI}. It's in the List. It took {bin_search_steps} Binary Search steps!"
            break;
        elif len(List)==1:
            if user_input not in List:
                return f"Sorry {UI} is not in the List. It took {bin_search_steps} Binary Search steps!"; 
        elif user_input < mid_number:
            List = List[:midIndx(List)];
            mid_number = List[midIndx(List)];
        elif user_input > mid_number:
            List = List[midIndx(List):];
            mid_number = List[midIndx(List)];   
        bin_search_steps += 1;
"""List [1-50]"""
# ~ L = [i for i in range(1,51)]; 
"""List [1-10000000]"""
# ~ L = [i for i in range(1,10**7+1)]

L= [1,2,3,5,6,8,9,10,11,15,17,20,22,25,27,30,100] # Current List

# ~ print(inside(L,UI)); #search NOT using binary seach

"""Optional checks, List, Len, midle index"""
# ~ print(f"Len of list = {len(L)}");
# ~ print(f"The List ==...\n{L}");
# ~ print(f" mid Indx {midIndx(L)}");

"""Call Binary seach function"""
UI = int(input("Hi! Is your number in list? Type here: "));
print(binarySearch(L,UI));
