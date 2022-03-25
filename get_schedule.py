import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import urllib.request, urllib.error
general_club ='https://websites.mygameday.app/club_info.cgi?c=0-4028-50167-599091-25666750'
 

   
def get_id(team):
    r = requests.get(general_club)
    c = r.content
    soup = BeautifulSoup(c,"lxml")
    a = soup.find_all('a', href=True, text=re.compile(team,re.I))
    s ='https://websites.mygameday.app/'
    l = []
    for i in a:
        b = str(i.get('href'))
        st = s + b
        response = urllib.request.urlopen(st)
        #webbrowser.open(st)
        l.append(st)
        #print(st)
    return l


#get_id('wakanda')

def run_script(): 
    site = get_id('wakanda')
    l = []
    try:
        
        for i in site:
            r = requests.get(i)
            c = r.content
            s = BeautifulSoup(c,"lxml")
            a = s.find_all("div",{"id":"teamhome-next-wrap"})
            for j in a:
                d ={}
                d["Date and Time"] = j.find("div",{"class":"sptime"}).text.replace(u'\xa0', u' ')
                d["Team"] = j.find("span",{"class": re.compile('(team2name|team1name)')}).text
                l.append(d)
        print(l)
    except Exception:
        pass
run_script()