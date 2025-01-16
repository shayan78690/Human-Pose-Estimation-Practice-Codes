import cv2

img = cv2.imread(r'humanposetest.jpg', 1)
print(img)

cv2.imshow('color_image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()