from random import randint;
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [randint(0,1000) for i in range(100)];
b = [randint(0,1000) for i in range(100)];
print(list(set(i for i in a if i in b)));
