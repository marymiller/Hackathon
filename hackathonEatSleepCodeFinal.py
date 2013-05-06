#Prepare yourself for the worst written code you have ever seen somehow it works I think we dont even know anymore
#Thank you

#By: Eat, Sleep, Code   -   Robert Rizzacasa, Mary Miller, Zach Meath

import socket
import math
import sys
import os


text2 = ""
counter = 0

#profit vars
profita=0
profitb=0
profitc=0
profitd=0

#cost constants
costa=0
costb=0
costc=0
costd=0

#Distrobution vars
dista=0
distb=0
distc=0
distd=0
diste=0
distf=0
distg=0
disth=0
disti=0

#demand vars
demanda=""
demandb=0
demandc=0
demandd=0
demande=0
demandf=0
demandg=0


configa=0
configb=0
configc=0
configd=0
confige=0
configf=0
configg=0
configh=0
configi=0

#control vars - get reset - passed to server
controla = 0
controlb = 0
controlc = 0
controld = 0
controle = 0
controlf = 0
controlg = 0
controlh = 0
controli = 0


#recieve cost vars
def cost(text):
    #use global vars and reset text and counter
    global counter
    global text2
    text2 = ''
    counter = 0
    global costa
    global costb
    global costc
    global costd
    #3 4 8 17
    text = text[6:]   #take out 'COSTS '
    #loop to set string input to int vars
    while(len(text)!=0):
        while(len(text)> 0 and text[:1] != " "):
            text2 = text2 + text[0]
            text = text[1:]
        text = text[1:]
        if counter == 0:
            costa = int(float(text2))
        if counter == 1:
            costb = int(float(text2))
        if counter == 2:
            costc = int(float(text2))
        if counter == 3:
            costd = int(float(text2))
        counter+=1
        text2 = ""

#recieve config vars
def config(text):
    global counter
    global text2
    text2 = ''
    counter = 0
    global configa
    global configb
    global configc
    global configd
    global confige
    global configf
    global configg
    global configh
    global configi
    text = text[7:]
    while(len(text)!=0):
        while(len(text)> 0 and text[:1] != " "):
            text2 = text2 + text[0]
            text = text[1:]
        text = text[1:]
        if counter == 0:
            configa = int(float(text2))
        if counter == 1:
            configb = int(float(text2))
        if counter == 2:
            configc = int(float(text2))
        if counter == 3:
            configd = int(float(text2))
        if counter == 4:
            confige = int(float(text2))
        if counter == 5:
            configf = int(float(text2))
        if counter == 6:
            configg = int(float(text2))
        if counter == 7:
            configh = int(float(text2))
        if counter == 8:
            configi = int(float(text2))
        counter+=1
        text2 = ""



#recieve demand vars
def demand(text):
    global counter
    global text2
    text2 = ''
    counter = 0
    global demanda
    global demandb
    global demandc
    global demandd
    global demande
    global demandf
    global demandg
    global demandh
    global demandi
    text = text[7:]
    while(len(text)!=0):
        while(len(text)> 0 and text[:1] != " "):
            text2 = text2 + text[0]
            text = text[1:]
        text = text[1:]
        if counter == 0:
            demanda = text2
        if counter == 1:
            demandb = int(float(text2))
        if counter == 2:
            demandc = int(float(text2))
        if counter == 3:
            demandd = int(float(text2))
        if counter == 4:
            if demande == 0:
                demande = int(float(text2))
            else:
                demande = (demande + int(float(text2))) / 2
        if counter == 5:
            if demandf == 0:
                demandf = int(float(text2))
            else:
                demandf = (demandf + int(float(text2))) / 2
        if counter == 6:
            if demandg == 0:
                demandg = int(float(text2))
            else:
                demandg = (demandg + int(float(text2))) / 2
        counter+=1
        text2 = ""






#recieve dist vars
def dist(text):
    global counter
    global text2
    text2 = ''
    counter = 0
    global dista
    global distb
    global distc
    global distd
    global diste
    global distf
    global distg
    global disth
    global disti
    text = text[5:]
    while(len(text)!=0):
        while(len(text)> 0 and text[:1] != " "):
            text2 = text2 + text[0]
            text = text[1:]
        text = text[1:]
        if counter == 0:
            dista = int(float(text2))
        if counter == 1:
            distb = int(float(text2))
        if counter == 2:
            distc = int(float(text2))
        if counter == 3:
            distd = int(float(text2))
        if counter == 4:
            diste = int(float(text2))
        if counter == 5:
            distf = int(float(text2))
        if counter == 6:
            distg = int(float(text2))
        if counter == 7:
            disth = int(float(text2))
        if counter == 8:
            disti = int(float(text2))
        counter+=1
        text2 = ""




#recieve profit vars
def profit(text):
    global counter
    global text2
    text2 = ''
    counter = 0
    global profita
    global profitb
    global profitc
    global profitd

    text = text[7:]
    while(len(text)!=0):
        while(len(text)> 0 and text[:1] != " "):
            text2 = text2 + text[0]
            text = text[1:]
        text = text[1:]
        if counter == 0:
            profita = int(float(text2))
        if counter == 1:
            profitb = int(float(text2))
        if counter == 3:
            profitc = int(float(text2))
        if counter == 4:
            profitd = int(float(text2))
        if counter == 5:
            profite = int(float(text2))
        counter+=1
        text2 = ""
        
#calculate changes to be made and returns output to be sent to server
def control():
    global controla
    global controlb
    global controlc
    global controld
    global controle
    global controlf
    global controlg
    global controlh
    global controli
    global targd
    global targe
    global targf
    global targg
    global targh
    global targi


    #calculate first tier changes - WEB
    freespacex = configa*180 - demande + 90
    freespacey = configb*180 - demandf + 90
    freespacez = configc*180 - demandg + 90
    while freespacex >= 200 and configa >0:
        controla -= 1
        freespacex = freespacex-180
    while freespacey >= 200 and configb >0:
        controlb -= 1
        freespacey = freespacey-180
    while freespacez >= 200 and configc >0:
        controlc -= 1
        freespacez = freespacez-180
    while freespacex <= 50:
        controla +=1
        freespacex+=100
    while freespacey <= 50:
        controlb +=1
        freespacey+=100
    while freespacez <= 50:
        controlc +=1
        freespacez+=100

    #calc second tier changes - JAVA
    freespacex = configd*400 - demande +200
    freespacey = confige*400 - demandf +200
    freespacez = configf*400 - demandg +200
    
    while freespacex >= 400 and configd > 0:
        controld -= 1
        freespacex = freespacex-400
    while freespacey >= 400 and confige >0:
        controle -= 1
        freespacey = freespacey-400
    while freespacez >= 400 and configf >0:
        controlf -= 1
        freespacez = freespacez-400
        
    while freespacex < 70:
        controld +=1
        freespacex+=300
    while freespacey < 70:
        controle +=1
        freespacey+=300
    while freespacez < 70:
        controlf +=1
        freespacez+=300

    #calc third tier changes - DB
    demand = demande + demandf + demandg
    freespace = ((configg+configh+configi) * 1000)
    
    if (demand >= freespace + 600):
        if configa>configb:
            controlg+=1
        else:
            controlh += 1

    if ((demand <= freespace - 400)):
        if configa>configb:
            if configh > 0:
                controlh -= 1
            elif configg > 0:
                
                controlg -= 1
        if configb>=configa:
            if configg>0:
                controlg-=1
            elif configh>0:
                controlh-=1

    

        
    return "CONTROL " + str(controla) + " " + str(controlb) + " " + str(controlc) + " " + str(controld) + " " + str(controle) + " " + str(controlf) + " " + str(controlg) + " " + str(controlh) + " " + str(controli)





#Start of program
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("hackathon.hopto.org", 18178))
#ports:
#1 day :  18178
#3 day :  18179
#10 day : 63333
s.send("INIT EatSleepCode")
print s.recv(4096)
s.send("RECD")
cost(s.recv(4096))
s.send("START")
y=0
conf = s.recv(4096)
#loop to run while still input
while conf is not "END" and y<2880:
    #2880 = 1
    #8640 = 3
    #28800 = 10
    x = 0
    while(x<7 and conf is not "END"):
        config(conf)
        s.send("RECD")
        demand(s.recv(4096))
        s.send("RECD")
        dist(s.recv(4096))
        s.send("RECD")
        profit(s.recv(4096))
        s.send("CONTROL 0 0 0 0 0 0 0 0 0")
        x+=1
        conf = s.recv(4096)
    #calc changes for every 8
    if conf is not "END":
        y+=x+1
        config(conf)
        s.send("RECD")
        demand(s.recv(4096))
        s.send("RECD")
        dist(s.recv(4096))
        s.send("RECD")
        profit(s.recv(4096))
        s.send(control())
        conf = s.recv(4096)



    z=0
    while z<40:
        print ""
        z+=1   
    
    print "Turn Number:  " + str(y) 
    print ""
    demande=0
    demandf=0
    demandg=0
  
    print "Total profit:  $" + str(profitc) + ".00"
    
    print "Overall percent of profit:  " + str(profitd)+ "%"
    print "NA-W  " + str(configa) + "  EU-W  " + str(configb) + "  AP-W  " + str(configc) + " \nNA-J  " + str(configd) + "  EU-J  " + str(confige) + "  AP-J  " + str(configf) + " \nNA-D  " + str(configg) + "  EU-D  " + str(configh) + "  AP-D  " + str(configi) 
    controla=0
    controlb=0
    controlc=0
    controld=0
    controle=0
    controlf=0
    controlg=0
    controlh=0
    controli=0
s.send("STOP")
s.close()

