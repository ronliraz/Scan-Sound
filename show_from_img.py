import cv2

name = "img1.jpg"
name2 = "img2.jpg"
img = cv2.imread(name)
img2 = cv2.imread(name2)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.imshow('image2', img2)
# cv2.waitKey(0)
res = cv2.absdiff(img, img2)
cv2.imshow('diff', res)
cv2.waitKey(0)
# import pdb; pdb.set_trace()

