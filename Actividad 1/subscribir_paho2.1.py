import paho.mqtt.client as paho

#Declaramos los arreglos donde se almacenaran cada dato
frec_count = [2000,2000,2000,2000,2000,2000,2000]
nuc_count = [6,6,6,6,6,6,6]
uso_count = [5,5,5,5,5,5,5]
mem_count = [50,50,50,50,50,50,50]
proc_count = [6,6,6,6,6,6,6]

#Definimos las funciones para realziar las suscripciones y los mensajes
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):

    #Imprime y convierte el dato que lee
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    tot = str(msg.payload)
    tot = tot.split("'")
    print(tot[1])

    #Almacena la frecuencia de cada equipo
    if (msg.topic == "dafne/frec"):
        frec_count[0] = float(tot[1])
    if (msg.topic == "miles/frec"):
        frec_count[1] = float(tot[1])
#    if (msg.topic == "dafne_badillo/frec"):
#        frec_count[2] = float(tot[1])
    if (msg.topic == "victor/frec"):
        frec_count[3] = float(tot[1])
    if (msg.topic == "joseduardo/frec"):
        frec_count[4] = float(tot[1])
    if (msg.topic == "alonso/frec"):
        frec_count[5] = float(tot[1])
    if (msg.topic == "anthony/frec"):
        frec_count[6] = float(tot[1])

    #Almacena el numero de nucleos
    if (msg.topic == "dafne/nuc"):
        nuc_count[0] = float(tot[1])
    if (msg.topic == "miles/nuc"):
        nuc_count[1] = float(tot[1])
    if (msg.topic == "dafne_badillo/nuc"):
        nuc_count[2] = float(tot[1])
    if (msg.topic == "victor/nuc"):
        nuc_count[3] = float(tot[1])
    if (msg.topic == "joseduardo/nuc"):
        nuc_count[4] = float(tot[1])
    if (msg.topic == "alonso/nuc"):
        nuc_count[5] = float(tot[1])
    if (msg.topic == "anthony/nuc"):
        nuc_count[6] = float(tot[1])

    #Almacena el uso del CPU
    if (msg.topic == "dafne/uso"):
        uso_count[0] = float(tot[1])
    if (msg.topic == "miles/uso"):
        uso_count[1] = float(tot[1])
#    if (msg.topic == "dafne_badillo/uso"):
#        uso_count[2] = float(tot[1])
    if (msg.topic == "victor/uso"):
        uso_count[3] = float(tot[1])
    if (msg.topic == "joseduardo/uso"):
        uso_count[4] = float(tot[1])
    if (msg.topic == "alonso/uso"):
        uso_count[5] = float(tot[1])
    if (msg.topic == "anthony/uso"):
        uso_count[6] = float(tot[1])    

    #Almacena el uso de memoria RAM
    if (msg.topic == "dafne/mem"):
        mem_count[0] = float(tot[1])
    if (msg.topic == "miles/mem"):
        mem_count[1] = float(tot[1])
#    if (msg.topic == "dafne_badillo/mem"):
#        mem_count[2] = float(tot[1])
    if (msg.topic == "victor/mem"):
        mem_count[3] = float(tot[1])
    if (msg.topic == "joseduardo/mem"):
        mem_count[4] = float(tot[1])
    if (msg.topic == "alonso/mem"):
        mem_count[5] = float(tot[1])
    if (msg.topic == "anthony/mem"):
        mem_count[6] = float(tot[1])   

    #Almacen el programa que mas consume
    if (msg.topic == "dafne/proc"):
        proc_count[0] = str(tot[1])
    if (msg.topic == "miles/proc"):
        proc_count[1] = str(tot[1])
    if (msg.topic == "dafne_badillo/proc"):
        proc_count[2] = str(tot[1])
    if (msg.topic == "victor/proc"):
        proc_count[3] = str(tot[1])
    if (msg.topic == "joseduardo/proc"):
        proc_count[4] = str(tot[1])
    if (msg.topic == "alonso/proc"):
        proc_count[5] = str(tot[1])
    if (msg.topic == "anthony/proc"):
        proc_count[6] = str(tot[1])     

    #Imprimimos el maximo, minimo y el propio de cada medición

    print ("La frecuencia maxima es ", max(frec_count))
    print ("Mi frecuencia es ", frec_count[5])
    print ("La frecuencia minima es ", min(frec_count))

    print ("El mayor numero de nucleos es ", max(nuc_count))
    print ("Mi numero de nucleos es ", nuc_count[5])
    print ("El menor número de nucleos es ", min(nuc_count))

    print ("El mayor uso de CPU es ", max(uso_count))
    print ("Mi uso de CPU es", uso_count[5])
    print ("El menor uso  de CPU es ", min(uso_count))

    print ("La mayor RAM es ", max(mem_count))
    print("Mi uso de RAM es", mem_count[5])
    print ("La menor RAM es ", min(mem_count))

    print ("Los programas que mas consumen son")
    for item in proc_count:
        print(item)

#Nos suscribimos a cada uno de los aspectos de cada usuario
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
#client.username_pw_set("etorresr", "G4t0")
client.connect("broker.mqttdashboard.com", 1883)

client.subscribe("dafne/frec", qos=1)
client.subscribe("dafne/nuc", qos=1)
client.subscribe("dafne/uso", qos=1)
client.subscribe("dafne/mem", qos=1)
client.subscribe("dafne/proc", qos=1)

client.subscribe("miles/frec", qos=1)
client.subscribe("miles/nuc", qos=1)
client.subscribe("miles/uso", qos=1)
client.subscribe("miles/mem", qos=1)
client.subscribe("miles/proc", qos=1)

client.subscribe("dafne_badillo/frec", qos=1)
client.subscribe("dafne_badillo/nuc", qos=1)
client.subscribe("dafne_badillo/uso", qos=1)
client.subscribe("dafne_badillo/mem", qos=1)
client.subscribe("dafne_badillo/proc", qos=1)

client.subscribe("victor/frec", qos=1)
client.subscribe("victor/nuc", qos=1)
client.subscribe("victor/uso", qos=1)
client.subscribe("victor/mem", qos=1)
client.subscribe("victor/proc", qos=1)

client.subscribe("joseduardo/frec", qos=1)
client.subscribe("joseduardo/nuc", qos=1)
client.subscribe("joseduardo/uso", qos=1)
client.subscribe("joseduardo/mem", qos=1)
client.subscribe("joseduardo/proc", qos=1)

client.subscribe("alonso/frec", qos=1)
client.subscribe("alonso/nuc", qos=1)
client.subscribe("alonso/uso", qos=1)
client.subscribe("alonso/mem", qos=1)
client.subscribe("alonso/proc", qos=1)

client.subscribe("anthony/frec", qos=1)
client.subscribe("anthony/nuc", qos=1)
client.subscribe("anthony/uso", qos=1)
client.subscribe("anthony/mem", qos=1)
client.subscribe("anthony/proc", qos=1)

client.loop_forever()