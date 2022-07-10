import json
import random
import datetime


with open ("prices_quality_1.json", "r") as f :
    data = json.load(f)





listworth = []




index1 = 2
index2 = index1 + 1

for i in range (3175):
    index2 = index1 + 1
    print (type(data))
    dict_data1 = (data[index1])
    dict_data2 = (data[index2])
    print (dict_data1)
    print (type(dict_data1))
    print (len(data))
    
    item_name1 = dict_data1['item_id']
    city1 = dict_data1['city']
    quality1 = dict_data1['quality']
    sell_price_min1 = dict_data1['sell_price_min']
    sell_price_min_date1 = dict_data1['sell_price_min_date']
    buy_price_min1 = dict_data1['buy_price_min']
    buy_price_min_date1 = dict_data1['buy_price_min_date']
    
    item_name2 = dict_data2['item_id']
    city2 = dict_data2['city']
    quality2 = dict_data2['quality']
    sell_price_min2 = dict_data2['sell_price_min']
    sell_price_min_date2 = dict_data2['sell_price_min_date']
    buy_price_min2 = dict_data2['buy_price_min']
    buy_price_min_date2 = dict_data2['buy_price_min_date']
    
    #time management
    sell_price_min_date2 = sell_price_min_date2[11:19]
    buy_price_min_date1  = buy_price_min_date1 [11:19]
    hour_caerleon = int(sell_price_min_date2[0:2])
    min_caerleon = int(sell_price_min_date2[3:5])
    hour_blackmarket = int(buy_price_min_date1[0:2])
    min_blackmarket  = int(buy_price_min_date1[3:5])
    time_caerleon = hour_caerleon*3600 + min_caerleon*60
    time_blackmarket = hour_blackmarket*3600 + min_blackmarket*60
    now = datetime.datetime.now()
    hour_now = now.strftime("%H")
    min_now  = now.strftime("%M")
    time_now = int(hour_now)*3600 + int(min_now)*60
    difference_time = abs(time_blackmarket - time_caerleon)
    difference_now_bm = abs(time_blackmarket - time_now)
    print (difference_now_bm)
    print ("Difference time between two markets is : "+str(difference_time))
    print ("The time now in seconds is "+ str(time_now))

    print (sell_price_min_date2, buy_price_min_date1)
    if buy_price_min1 > sell_price_min2 and sell_price_min2 != 0 :
        difference = buy_price_min1 - sell_price_min2
        print ("Worth")
        if difference >= 5000 and difference_now_bm <=3600 :
            listworth.append(item_name1)
            listworth.append(difference)
    index1 += 2
    

print (listworth)