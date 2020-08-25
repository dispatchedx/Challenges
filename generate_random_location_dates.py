import os
import random
from datetime import datetime
from random import randrange
data= '{ "locations" :['

for i in range(15000):
    timestamp=random.randint(1420070400000 ,1598358416123 )
    activities=["WALKING","STILL","ON_BICYCLE","RUNNING","IN_VEHICLE"]
    activity=activities[randrange(4)]

    data = data + '{ "timestampMs" : "'+str(timestamp)+'","latitudeE7" : 381852128,"longitudeE7" : 217105715,"accuracy" : 64,"activity" : [ {"timestampMs" : "'+str(timestamp)+'","activity" : [ {"type" : "'+activity+'", "confidence" : 100 } ] } ]},' #remove this last traling comma


data = data + "]}"

with open('kek.json','w') as file:
    file.write(data)



