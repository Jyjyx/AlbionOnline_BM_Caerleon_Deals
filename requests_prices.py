import requests 
import pyperclip
from items_id import damien
import json

number_items_list = 1
number_right = 106



with open("prices_quality_1.json", "w")as file:
    file.write("[")


for i in range (3204):


    damien[number_items_list] = f"{damien[number_items_list]},"
    number_items_list += 1



print (damien)
print (type(damien))
avancement = 0

number_left = 0
for i in range (30):
    liste = damien[number_left:number_right]
    liste = " ".join(liste)
    liste = liste.replace(" ","")
    url = (f"https://www.albion-online-data.com/api/v2/stats/Prices/{liste}?locations=Caerleon,BlackMarket&qualities=1")
    r = requests.get(url)
    print (f"processing {avancement}%" )  
    with open("prices_quality_1.json", "a") as file:
        if avancement == 0:
            print("I don't write the first coma")
        else:
            file.write(",")
        file.write(r.text.replace("[", "").replace("]",""))
    liste = liste.split(" ")
    print (number_right)
    print (number_left)
    number_right += 106
    number_left = number_right - 106
    avancement += 3.3


with open("prices_quality_1.json", "a") as file:
    file.write("]")