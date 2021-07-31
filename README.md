# Ridler-Calvard Thresholding Method
Ridler-Calvard thresholding method is an iterative approach that finds optimum threshold value. 
In this approach, an initial threshold value is determined in the first step. 
This initial threshold value is found by calculating the average of pixel values of the image. 
The average of pixel values of image is calculated by the equation 1. <br>
![GitHub Logo](/images/equation1.jpg)
After the first threshold value is determined, values lower than the threshold value are divided into two parts as background and higher values as foreground. 
Then, the mean of the pixel values of the background and foreground is calculated as µ1 and µ2, respectively, as shown in equation 1. 
Subsequently, new threshold value is calculated by the equation 2.
![GitHub Logo](/images/equation2.jpg)
Then again, values lower than the threshold value are divided into two parts as background and higher values as foreground. 
The average of the pixel values of these two parts is recalculated and a new threshold value is calculated with equation 2. 
This cycle continues until there is little or no change in the threshold value. At the end of the loop, the final threshold value is found.
<br>
### Original Image
![GitHub Logo](/images/plane.jpg)
<br>
### Output:
Threshold value was calculated 134.84 by using ridler-calvard.py<br>
![GitHub Logo](/images/plane_binary.jpg)
