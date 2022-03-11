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
    a = soup.find('a', href=True, text=re.compile(team,re.I))
    s ='https://websites.mygameday.app/'
    b = str(a.get('href'))
    st = s + b
    try:
        response = urllib.request.urlopen(st) 
        
        return st
    except Exception as e:            
        print()

    #webbrowser.open(get_id(team))
   

