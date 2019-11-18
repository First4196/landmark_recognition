#usage
#place this python script in the same directory as image directory
#this script will make a subfolder to store the resized image

########## This resizer will solely use old fashioned resize ##########

########## Set path here #########
PATH = 'resized'
########## Set path here #########
import cv2, os

if not os.path.exists(PATH):
    os.mkdir(PATH)

for img in os.listdir():
    if img[-1] != 'g': continue
    print(img)
    image = cv2.imread(img)
    image = cv2.resize(image, (320, 240))
    cv2.imwrite(PATH+'/'+img, image)