import cv2

img = cv2.imread(r'india.jpg', 1)
print('Original Dimensions : ', img.shape)

width = 350
height = 450
dim = (width, height)
#resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimesnsions : ', resized.shape)
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()