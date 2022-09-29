a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a);
UI = int(input("Find number less than 'X' you list above. Your NR.. "))
nl = [i for i in a if i < UI];
print(nl);


