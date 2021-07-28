from cv2 import cv2
ROOTDIR="/../../";#Directory of an image
img=cv2.imread(ROOTDIR,0)#imread the image as grayscale.
rows= img.shape[0]
cols=img.shape[1]
resolution=rows*cols#resolution of the image
total=0
for i in range(0,rows):
    for j in range(0,cols):
        total=total+img[i,j]
mean=total/resolution

#while loop to calculate the threshold value.
#fg represents the foreground
#bg represents the background
while(True):
    total_fg=0
    total_bg=0
    count_fg=0
    count_bg=0
    for i in range(0,rows):
        for j in range(0,cols):
            if(img[i,j]<mean):
                total_fg=total_fg+img[i,j]
                count_fg=count_fg+1
            else:
                total_bg=total_bg+img[i,j]
                count_bg=count_bg+1
    mean_fg=total_fg/count_fg
    mean_bg=total_bg/count_bg
    T=(mean_fg+mean_bg)/2
    if(mean==T):
        break
    else:
        mean=T

print("Threshold Value:",T)

#if the pixel value less than threshold value, the new pixel value will be 0,
#if the pixel value greater than threshold value, the new pixel value will be 255.
for i in range(0,rows):
    for j in range(0,cols):
        if img[i,j]<T:
            img[i,j]=0
        else:
            img[i,j]=255
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()