import argparse
import cv2
import numpy as np


img=cv2.imread("IMAGES/Nike-crop.jpeg")
corner=img[:,:]
cv2.imshow("IMAGES/Nike-crop.jpeg",corner)
cv2.waitKey(0)
cv2.destroyAllWindows()


print(img.shape[1])


(b,g,r)=img[0,0]
print(b,g,r)


cv2.imshow("img1",img[0:100,0:100])
cv2.waitKey(0)
cv2.destroyAllWindows()


img[0:100,0:100]=(0,0,255)
cv2.imshow("img1",img[0:100,0:100])
cv2.waitKey(0)
cv2.destroyAllWindows()


canvas=np.zeros((300,300,3),dtype="uint8")



green=(0,255,0)
red=(0,0,255)
cv2.line(canvas,(0,0),(300,300),green,3)
cv2.imshow("img2",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.line(canvas,(300,0),(0,300),red,7)
cv2.imshow("img2",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


blue=(255,0,0)
cv2.rectangle(canvas,(100,50),(200,200),blue,5)
cv2.imshow("img3",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


saffron=(0,0,128)
cv2.rectangle(canvas,(150,0),(20,200),saffron,-1)
cv2.imshow("img3",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()



canvas=np.zeros((300,300,3),dtype="uint8")

white=(255,255,255)
for r in range(0,180,10):
    cv2.circle(canvas,(150,150),r,white)
    
cv2.imshow("img3",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


canvas1=np.zeros((300,300,3),dtype="uint8")
for i in range(0,30):
    color=np.random.randint(0,high=255,size=(3,)).tolist()
    center=np.random.randint(0,high=300,size=(2,))
    radius=np.random.randint(5,high=200)
    cv2.circle(canvas1, tuple(center), radius,color, -1)
cv2.imshow("imgs",canvas1)
cv2.waitKey(0)
cv2.destroyAllWindows()




M=np.float32([[1,0,50],[0,1,90]])
shifted= cv2.warpAffine(img,M,(img.shape[1]+500,img.shape[0]+500))
cv2.imshow("imgeudhe",shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()




M=np.float32([[1,0,-50],[0,1,-40]])
shifted= cv2.warpAffine(img,M,(img.shape[1]+500,img.shape[0]+500))
cv2.imshow("imgeudhe",shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()



(h,w)=img.shape[:2]
center=(w/2,h/2)
M=cv2.getRotationMatrix2D(center,45,1.0)



IMAGE=cv2.warpAffine(img,M,(w+100,h+100))
cv2.imshow("IMAGE",IMAGE)
cv2.waitKey(0)
cv2.destroyAllWindows()


r=300/img.shape[1]
dim=(300,int(r*img.shape[0]))
resize=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Img",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


flip=cv2.flip(img,0)
cv2.imshow("flip",flip)
cv2.waitKey(0)
cv2.destroyAllWindows()



M=np.ones(img.shape,dtype="uint8")*100
add=cv2.add(img,M)
cv2.imshow("add",add)
cv2.waitKey(0)
cv2.destroyAllWindows()



M=np.ones(img.shape,dtype="uint8")*50
subtract=cv2.subtract(img,M)
cv2.imshow("subtract",subtract)
cv2.waitKey(0)
cv2.destroyAllWindows()



M=np.ones(img.shape,dtype="uint8")*50
subtract=(img-M)
cv2.imshow("subtract",subtract)
cv2.waitKey(0)
cv2.destroyAllWindows()



