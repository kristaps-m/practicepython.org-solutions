n = int(input(" Give me a number and i will give u divisoors!... "));
L = [];
for i in range(1,n+1):
    if n % i == 0:
        L.append(i);
print(L);
