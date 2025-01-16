import cv2

img = cv2.imread(r'humanposetest.jpg', 0)
print(img)
status = cv2.imwrite('save.jpg', img)
print("Image written to file system: ", status)