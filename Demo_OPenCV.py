
"""
Step1: Import cv2 packagee (python - open cv)
Step2: Create an object and pass image ref
Step3: Display image using imshow()
Step4: Close all Window
"""
import cv2

image = cv2.imread("ross1.PNG",)

window_name = 'image'

cv2.imshow(window_name,image)


cv2.waitKey(0)
cv2.destroyAllWindows()