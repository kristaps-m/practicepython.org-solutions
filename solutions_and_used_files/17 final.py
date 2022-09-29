# 17-decode-a-web-page
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

print(urls);

for i in urls:
    print(i);


