from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import urllib.request
amaz_url=r"https://www.amazon.in/laptop/s?k=laptop"
response_obj=urllib.request.urlopen(amaz_url)
print(response_obj)
soup=BeautifulSoup(response_obj,'html.parser')
link=soup.find_all("span",{'class':"a-size-medium a-color-base a-text-normal" })
lines = [  span.get_text() for span in link]
for line in lines:
    lis=line.split()
    print(lis[0])