# Birthday Plots
# https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

import json;
from collections import Counter;

from bokeh.plotting import figure, show, output_file;

#-------------------------------------------------------
with open("exercise 34 info.json", "r") as f:
    info = json.load(f)
    
Dictionary = {"01":"January","02":"February","03":"March","04":"April",
"05":"May","06":"June","07":"July","08":"August",
"09":"September","10":"October","11":"November","12":"December"}

List_of_months = [];

for i in info.values():
    m = i.split(".")[1];
    List_of_months.append(Dictionary[m]);
    
"""Print counted months"""
print("");
for k,v in Counter(List_of_months).items():
    print(f"{k}: {v}");
#-------------------------------------------------------


output_file("plot.html")
x_categories = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
x = [];
y = [];
#--------------------------
for k,v in Counter(List_of_months).items():
    x.append(k);
    y.append(v);
#--------------------------
 # plot_width=800 should be ideal for this exercise
p = figure(x_range=x_categories,plot_width=70*len(x_categories));
p.vbar(x=x, top=y, width=0.5) # width=0.5 was

show(p)


"""
output_file("plot.html")
x_categories = ["Pirmdiena", "Otrdiena", "Tresdiena", "Ceturtdiena", "Piektdiena"]
x = ["Pirmdiena", "Ceturtdiena", "Piektdiena"]
y = [4, 5, 6]

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

show(p)




# we specify an HTML file where the output will go
output_file("plot.html")

# load our x and y data
x = [10, 20, 30]
y = [4, 5, 6]

# create a figure
p = figure()

# create a histogram
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)"""



