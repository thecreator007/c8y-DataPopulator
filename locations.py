import requests
import json
def data_populator(name,status,lng,lat,serial):
   #example hostname:https://developer.cumulocity.com
   urlmo="<<hostname>>"
   da1={  
      "name":name,
      "type":"c8y_Linux",
      "c8y_IsDevice":{  

      },
      "com_cumulocity_model_Agent":{  

      },
      "com_softwareag_parkingpi_ParkingPiStatus": {
         "status": status
         },
      "c8y_SupportedOperations":[  
         "c8y_RemoteAccessConnect",
         "c8y_Restart",
         "c8y_Firmware",
         "c8y_Configuration",
         "c8y_SoftwareList"
      ],
      "c8y_Position":{  
         "lng":lng,
         "lat":lat
      },
      "c8y_Hardware":{  
         "serialNumber":serial,
         "model":"BCM2835",
         "revision":"ma2018"
      }
   }
   head={
   	 "Content-Type": "application/json",
       	"Accept": "application/json",
   }
   s1=requests.post(urlmo,json=da1,auth=('<<username>>','<<password>>'),headers=head)
   print(s1)
   t=s1.json()
   ids=t["id"]
   return ids
def data_register(ids,exname):
   #example hostname:https://developer.cumulocity.com
   urlre="<<hostname>>/identity/globalIds/"+ids+"/externalIds"
   da1={
       "type" : "c8y_Serial",
       "externalId" : exname
   }
   head={
       "Content-Type": "application/json",
         "Accept": "application/json",
   }
   s1=requests.post(urlre,json=da1,auth=('<<username>>','<<username>>'),headers=head)
   print(s1)
with open("data.json") as c:
      dumdata=json.load(c)
n=len(dumdata["devices"])
i=0
while i<n:
   name=dumdata["devices"][i]["Name"]
   status=dumdata["devices"][i]["status"]
   exname=dumdata["devices"][i]["exname"]
   lng=dumdata["devices"][i]["lng"]
   lat=dumdata["devices"][i]["lat"]
   serial=dumdata["devices"][i]["serial"]
   ids=data_populator(name,status,lng,lat,serial)
   data_register(ids,exname)
   i+=1

   

