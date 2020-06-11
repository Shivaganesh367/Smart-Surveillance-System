import numpy as np


from gpiozero import Buzzer
from time import sleep


buzzer = Buzzer(17)

label = [] #Labels or objects are detected and initialized in the numpy array
with open('array.txt','r') as f:
    for line in f:
        objects = [elt.strip() for elt in line.split(',')]
        label.append(objects)
label = np.array(label)


Face = []
with open('Face_recognition.txt','r') as file:
    for line in file:
        expressions = [elt.strip() for elt in line.split(',')]
        Face.append(expressions)
Face = np.array(Face)
        
        

for detect in label:
    for detection in Face:
        if(detect == 'Firearm' or detect == 'Rifle' or detect == 'Airsoft' or detect == 'Trigger' or detect == 'Gun' or detect == 'Airsoft gun' or detect == 'Knife' or detect == 'Melee weapon' or detect =='Cold weapon' ):
            if(detection == 'Fear' or detection == 'Crying'):
                buzzer.on()
                sleep(2)
                buzzer.off()