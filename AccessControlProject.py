import os

import cv2
import face_recognition

path = 'ImagesAccess'
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)  # checking contents
for cl in mylist:
    curImage = cv2.imread(f'{path}/{cl}')
    images.append(curImage)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)  # checking contents after split

imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
