import requests
import bs4
import time 
from win10toast import ToastNotifier 

# create an object to ToastNotifier class 
n = ToastNotifier() 

    
    
    


def sendmessage(title, message):
    n.show_toast(title,message,duration=6,icon_path="not.ico")
    

def selectMatch():
    url='https://www.cricbuzz.com/'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    li=[]
    ti=[]
    deatails = soup.select(".cb-mat-mnu")
    for link in deatails[0].findAll('a'):
        li.append(link.get('href'))
    for title in deatails[0].findAll('a'):
        ti.append(title.get('title'))
    print("Select the match you want")
    for  i in range(1,len(ti)-1):
        print(i,ti[i])

    option= int(input("Enter your number :"))
    

    retUrl =url[:-1]+li[option]
    
    return retUrl


def score():
    url = selectMatch()
    url=url.replace('-scores','-scorecard',1)
    loo=0
    while (loo<1):
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        deatails = soup.select(".cb-col .cb-col-100 .cb-scrd-hdr-rw")
        s=""
        for i in deatails:
            s+=" "+i.getText()+"\n"
        print(s)  
        sendmessage("CricDesk",s)
        loo=loo+1
        time.sleep(5)
    
score()
