import schedule
import time
import os
import sys

os.system('node g.js https://dogcorp.co/LOGIN http.txt 600 GET PHPSESSID:8317q59mirfeg4sb66abkgbo73')

def job():
    os.system('node g.js https://dogcorp.co/LOGIN http.txt 600 GET PHPSESSID:8317q59mirfeg4sb66abkgbo73')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)