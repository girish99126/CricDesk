import requests
import bs4
import time 
from win10toast import ToastNotifier 

# create an object to ToastNotifier class 
n = ToastNotifier() 

    
    
    

#This Fucnction is for to send the toast messages
def sendmessage(score,time):
    n.show_toast("CricDesk",score,duration=time,icon_path="not.ico")
    
#From the list of options select the option
'''
It show the match in cricbuzz
and display here
'''
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


'''

To get score this function get the url and extract the xml and display
the text (score) in that class
'''

def score():
    url = selectMatch()
    url=url.replace('-scores','-scorecard',1)
    n=0
    while (n<1000):
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        details = soup.select(".cb-col .cb-col-100 .cb-scrd-hdr-rw")
        score=""
        for i in details:
            score+=" "+i.getText()+"\n"  
        sendmessage(score,5)
        n=n+1
        time.sleep(20)
    
score()
