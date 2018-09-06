import cv2
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imwrite("gray_image.jpg",gray)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#cv2.imwrite("hsv_image.jpg",hsv)
bgr = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
#cv2.imwrite("bgr_image.jpg",bgr)

yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
#cv2.imwrite("yuv_image.jpg",yuv)

gray_bgr = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#cv2.imwrite("gray2bgr.jpg",gray_bgr)


