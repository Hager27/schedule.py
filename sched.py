

import schedule
import time
import requests
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
page = requests.get(url)
data =page.json()
def bitcoin():
    print("fetching bitcoin price ")
    result = data['bpi']['USD']
    print(result)
def task():

    print("its time for arrival of customer")

def appoint():
    print("its your appointment to the court")

def OUt():
    print("Its time to get out of office")

#Time

schedule.every(5).seconds.do(bitcoin)
schedule.every(5).seconds.do(task)
schedule.every(10).seconds.do(appoint)
schedule.every().day.at("11:00").do(OUt)

while True:
    schedule.run_pending()
    time.sleep(1)
