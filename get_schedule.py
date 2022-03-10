import requests
from bs4 import BeautifulSoup

parra_team ='https://websites.mygameday.app/team_info.cgi?id=12784093&c=0-4028-0-598757-0'

def get_schedule():
    try:
        r = requests.get(parra_team)
        c = r.content
        s = BeautifulSoup(c,"html.parser")
        a = s.findAll("div",{"id":"teamhome-next-wrap"})
        for i in a:
            d ={}
            d["Date and Time"] = i.find("div",{"class":"sptime"}).text.replace(u'\xa0', u' ') 
        return d["Date and Time"]
    except Exception as e:
        print()

       

get_schedule()