# Write To A File
# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

# CODE FROM: "17-decode-a-web-page"
"""File to write to will go where your 20.py file is"""

import requests
from bs4 import BeautifulSoup
result = requests.get("https://www.nytimes.com/"); #https://www.delfi.lv/ #https://www.nytimes.com/
src = result.content;
soup = BeautifulSoup(src,"lxml");
urls = [];
for h3_tag in soup.find_all("h3"):
    urls.append(h3_tag.text);
    
for h2_tag in soup.find_all("h2"):
    urls.append(h2_tag.text);
    
for h1_tag in soup.find_all("h1"):
    urls.append(h1_tag.text);

# ~ print(urls);


for i in urls:
    print(i);

"""write to file?"""
print();
user_input = input("  >>>How do you want to call your file? .txt \n Type it here:  ")
f = open(f"{user_input}.txt","w");
"""I am trying to write from latvian websites. I failed :("""
for i in urls:
    try:
        i = i.replace("\r","").replace("\t","").replace("\n","").replace("\nPLUS","");
        f.write(i);
        f.write("\n")
    except:
        # ~ wierd = "".join(j for j in i if j.isalpha());
        f.write("Can't write this");
        f.write("\n")
f.close();



