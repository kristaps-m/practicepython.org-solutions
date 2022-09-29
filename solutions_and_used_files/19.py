# Decode A Web Page Two
# https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
# 17-decode-a-web-page
import requests
from bs4 import BeautifulSoup
result = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"); #https://www.delfi.lv/ #https://www.nytimes.com/
src = result.content;
soup = BeautifulSoup(src,"lxml");
texts = [];
for p_tag in soup.find_all("p"):
    texts.append(p_tag.text);

for i in texts:
    print(i);



