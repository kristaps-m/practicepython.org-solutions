UI = input("Give me a name: ... ");
print(UI == UI[::-1]);
s = "";
for i in reversed(UI):
    s+= i;
print(s.lower()==UI.lower());
