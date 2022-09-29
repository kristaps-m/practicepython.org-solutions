import json;
from collections import Counter;

with open("exercise 34 info.json", "r") as f:
    info = json.load(f)
print(info); # print from file!

Dictionary = {"01":"January","02":"February","03":"March","04":"April",
"05":"May","06":"June","07":"July","08":"August",
"09":"September","10":"October","11":"November","12":"December",
}
"""for next task 3 lines below"""
# ~ x_categories = [];
# ~ for i in Dictionary.values():
    # ~ x_categories.append(i)
    
List_of_months = []

for i in info.values():
    m = i.split(".")[1];
    List_of_months.append(Dictionary[m]);
    
# ~ print(List_of_months);
"""Print counted months"""
print("");
for k,v in Counter(List_of_months).items():
    print(f"{k}: {v}");
    
print(x_categories);

