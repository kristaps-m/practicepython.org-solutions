import random;
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [random.randint(0,100) for i in range(100)];
b = [random.randint(0,100) for i in range(100)];
print(a)
print(b)
el = list(set([i for i in a if i in b]));
print(el);
