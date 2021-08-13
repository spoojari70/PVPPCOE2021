"""
Step1: Import openCV/cv2
Step2: use Frontal Face Classifier for recognising Face from image
Step3: Reading image  using imread()
Step4: Marking Face using Color
Step5: Displaying image with marked pattern

"""


import  cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("Parth.jpg")

gray_Img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_Img,scaleFactor=2.05,minNeighbors=5)

for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,250,0),3)
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()