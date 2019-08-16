import cv2
image=cv2.imread("dinesh.jpg")
i=cv2.imread("d.jpg")
(h,w,l)=image.shape
#print("width={},heigth={},length={}".format(h,w,l))
cv2.imshow("NATURE",image)
cv2.imshow("NATURE",i)
cv2.waitKey(0)
cv2.waitKey(0)