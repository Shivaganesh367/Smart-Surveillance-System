from  gpiozero import Buzzer
from time import sleep

import picamera
import os
from PIL import Image, ImageDraw

buzzer = Buzzer(17)


from google.cloud import vision
client = vision.ImageAnnotatorClient()
image_name = 'image.jpg'

def takephoto():
    camera = picamera.PiCamera()
    camera.capture(image_name)

def draw_face_rectangle(image_in, rect_in):
    im = Image.open(image_in)
    f,e = os.path.splitext(image_in)
    image_out = f + "_out_boundrectangle" + e
    print("image out is named: "+ image_out)

    draw = ImageDraw.ImageDraw(im)
    draw.rectangle(rect_in)
    im.save(image_out)

def main():
    takephoto() 
    

    with open(image_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.types.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations
    #print(faces)
    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)


    response_label = client.label_detection(image=image)
    labels = response_label.label_annotations
    print('Labels:')
    obj = []

    for label in labels:
        obj.append(label.description)
        print(label.description)

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                    'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        detection["anger"] = likelihood_name[face.anger_likelihood]
        detection["joy"] = likelihood_name[face.joy_likelihood]
        detection["surprise"] = likelihood_name[face.surprise_likelihood]
        print(detection)
      '''  for detect in obj:
            
            if(((detection["anger"] == "VERY_UNLIKELY") and (detection["joy"] == "VERY_UNLIKELY") and (detection["surprise"] == "VERY_UNLIKELY")) or ((detection["anger"] == "VERY_UNLIKELY") and (detection["joy"] == "VERY_UNLIKELY") and (detection["surprise"] == "UNLIKELY")) and ((detect =="Firearm") or (detect == "Gun") or (detect == "Trigger") or(detect == "Airsoft") or (detect == "Airsoft gun") or (detect == "Assault rifle") or(detect == "Air gun") or (detect == "Rifle") or (detect == "Knife") or (detect == "Cold weapon") or (detect == "Kitchen knife") or (detect == "Bowie knife") or (detect == "Melee weapon") or (detect == "Blade") or (detect == "Huntingl knife"))):

                
                print("Fear")
                for i in range(2):
                    buzzer.on()
                    print("Beep")
                    sleep(0.5)
                
            if(((detection["anger"] == "VERY_UNLIKELY") and (detection["joy"] == "VERY_UNLIKELY") and (detection["surprise"] == "VERY_UNLIKELY")) or ((detection["anger"] == "VERY_UNLIKELY") and (detection["joy"] == "VERY_UNLIKELY") and (detection["surprise"] == "UNLIKELY")) and ((detect =="Firearm") or (detect == "Gun") or (detect == "Trigger") or(detect == "Airsoft") or (detect == "Airsoft gun") or (detect == "Assault rifle") or(detect == "Air gun") or (detect == "Rifle") or (detect == "Knife") or (detect == "Cold weapon") or (detect == "Kitchen knife") or (detect == "Bowie knife") or (detect == "Melee weapon") or (detect == "Blade") or (detect == "Huntingl knife"))):

                 print("Crying")
                 for i in range(2):
                    buzzer.on()
                    print("Beep")
                    sleep(0.5)'''
        
        
        

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        rectangle = []
        rectangle.append((face.bounding_poly.vertices[0].x,face.bounding_poly.vertices[0].y))
        rectangle.append((face.bounding_poly.vertices[2].x,face.bounding_poly.vertices[2].y))
        print('face bounds: {}'.format(','.join(vertices)))

        draw_face_rectangle(image_name, rectangle)



if __name__ == '__main__':

    main()