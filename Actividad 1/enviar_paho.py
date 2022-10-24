import paho.mqtt.client as paho
from random import randint
import time
import psutil

#Funcion para publicar 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
    
#Funcion para ver cual es la que mas consume
def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects

client = paho.Client()
#client.username_pw_set("alonso", "p1")
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

#Creamos un while para que cada 30 seg publique la informacion en el formato correcto
while True:
    listOfRunningProcess = getListOfProcessSortedByMemory()

    frec  = str(psutil.cpu_freq())
    frecc  = frec[17:23]

    memo = str(psutil.virtual_memory())
    memo = memo.split(",")
    memo = memo[2].split("=")

    pro = str(listOfRunningProcess[0])
    pro = pro.split(":") 
    pro = pro[3].split("'") 

    (rc, mid) = client.publish("alonso/frec", str(frecc), qos=1)
    (rc, mid) = client.publish("alonso/nuc", str(psutil.cpu_count()), qos=1)
    (rc, mid) = client.publish("alonso/uso", str(psutil.cpu_percent(4)), qos=1)
    (rc, mid) = client.publish("alonso/mem", str(memo[1]), qos=1)
    (rc, mid) = client.publish("alonso/proc", str(pro[1]), qos=1)
    print(frecc)
    print (memo[1])
    print(pro[1])
    
    time.sleep(30)
