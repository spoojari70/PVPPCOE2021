import cv2

image = cv2.imread("ross1.PNG",0)
resize_img = cv2.resize(image, (200,200))
cv2.imshow("Ross",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()