import cv2
#read image as grayscale
img = cv2.imread('india.jpg')
#get image heigth width
(h, w) = img.shape[:2]
#calculate the center of image
center = (w / 2, h / 2)

angle90 = 90
angle180 = 180
angle270 = 270

scale = 1.0

#Perform the counterclockwise rotation holding at the center
#90 degree
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

#180 degree
M = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M, (h, w))

#270 degree
M = cv2.getRotationMatrix2D(center, angle270, scale)
rotated270 = cv2.warpAffine(img, M, (h, w))

cv2.imshow('Original Image', img)
#cv2.waitKey(0) waits until a key is pressed
#cv2.destroyAllWindows() destroy the window showing image

cv2.imshow('Rotated 90 degrees', rotated90)

cv2.imshow('Rotated 180 degrees', rotated180)

cv2.imshow('Rotated 270 degrees', rotated270)

cv2.waitKey(0)
cv2.destroyAllWindows()

