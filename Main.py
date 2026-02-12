import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image

image = cv2.imread('mythpat.jpg')

# Convert to rgb for displaying with matplot lib

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Orignal image")
plt.show()

gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
plt.imshow(gray_image, cmap = 'gray')
plt.title("grayscale image")
plt.show()
cropped_image = image[100:300,200:400]
cropped_rgb = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped region")
plt.imshow()
(h,w)= image.shape[:2]
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
rotated_rgb = cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.title("Rotated Image")
plt.show()
brightness_matrix = np.ones(image.shape,dtype="uint8")
brighter = cv2.add(image,brightness_matrix)
brighter_rgb=cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("brighter image")
plt.show()
cv2.imwrite('output_images/grayscale_image.jpg',gray_image)
cv2.imwrite('output_images/cropped_image.jpg',cropped_image)
cv2.imwrite('output_images/rotated_image.jpg',rotated)
cv2.imwrite('output_images/brighter_image.jpg', brighter)
