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


def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodeListKnown = findEncodings(images)
print(len(encodeListKnown))

# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
#
# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeTest)
# print(results, faceDis)
# cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
