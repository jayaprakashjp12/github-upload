from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
url_cf=r"https://codeforces.com/ratings"
response_obj=urlopen(url_cf)
soup=BeautifulSoup(response_obj,'html.parser')
pipe=soup.find_all("tbody") 
for vik in pipe:
    link=vik.find_all("a",{'class':"rated-user user-legendary" })
    #link=soup.find_all("span",{'class':"a-size-medium a-color-base a-text-normal" })
    lines = [  span.get_text() for span in link]
    for line in lines:
        print(line)