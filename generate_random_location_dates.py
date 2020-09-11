
import random
from random import randrange
data = '{ "locations" :['

for i in range(15000):

    start_timestamp=1420070400000 #2015/8/25
    end_timestamp=1603843200000 # 2020/10/28
    #1598358416123 #2020/8/25
    timestamp=random.randint(start_timestamp ,end_timestamp )

    activities=["WALKING", "STILL", "ON_BICYCLE", "RUNNING", "IN_VEHICLE"]
    activity=activities[randrange(5)]

    data = data + '{ "timestampMs" : "'+str(timestamp)+'","latitudeE7" : 381852128,"longitudeE7" : 217105715,"accuracy" : 64,"activity" : [ {"timestampMs" : "'+str(timestamp)+'","activity" : [ {"type" : "'+activity+'", "confidence" : 100 } ] } ]},' #removing this last traling comma when it finishes


data = data[:-1] + "]}"

with open('lulw.json', 'w') as file:
    file.write(data)



