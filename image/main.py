import cv2
import matplotlib.pyplot as plt

image = cv2.imread('hi.png')
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_ = image.shape

arrow_start_left = (20,height-50)
arrow_end_right = (width-20,height-50)

cv2.arrowedLine(image_rgb,arrow_end_right,arrow_start_left,(240,145,160),3,tipLength=0.05)
cv2.arrowedLine(image_rgb,arrow_start_left,arrow_end_right,(255,145,160),3,tipLength=0.05)

width_label = (width//2-100,height-80)
cv2.putText(image_rgb,f'Width:{width}px',width_label,cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,145,160),2)

cv2.imwrite('hi.png',image_rgb)
plt.imshow(cv2.cvtColor(image_rgb,cv2.COLOR_BGR2RGB))
plt.title("annoted image with bidirectional arrows")
plt.axis('off')
plt.show()