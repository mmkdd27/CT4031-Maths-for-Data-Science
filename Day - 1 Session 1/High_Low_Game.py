import requests
import math
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
rnd_num = str(data["bpi"]["USD"]["rate"])

print (rnd_num[7],"Higher or lower?")
ans = input("[h/l]")
if ans == "h":
    if rnd_num[7] >= rnd_num[8]:
        print("it was lower ,you lost !")
    else:
        print("higher, you won!")

elif ans == "l":
    if rnd_num[7] >= rnd_num[8]:
        print("it was lower ,you won !")
    else:
        print("higher, you lost")
else:
    print("restart the program, i didn't build any error correction ")
