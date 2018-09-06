import cv2

img = cv2.imread("/home/bhavani/work/Python/spyder/CV/OpenCV/image.jpg")
cv2.imwrite("/home/bhavani/work/Python/spyder/CV/OpenCV/saved_image.jpg",img)
print("Image saved succesfully")
