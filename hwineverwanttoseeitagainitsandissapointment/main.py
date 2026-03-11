import cv2
import numpy as np 
import matplotlib.pyplot as plt

def display_image(title,image):

    plt.figure(figsize=(8,8))

    if len(image.shape) == 2:
        plt.imshow(image,cmap='gray')

    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_edge_detection(image,method="sobel",ksize=3,threshold1=100,threshold2=200):

    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    if method=="sobel":
        sobelx = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=ksize)
        sobely = cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=ksize)
        return cv2.bitwise_or(sobelx.astype(np.uint8),sobely.astype(np.uint8))
    
    elif method =="canny":
        return cv2.Canny(gray_image,threshold1,threshold2)
    
    elif method == "laplacian":
        return cv2.Laplacian(gray_image,cv2.CV_64F).astype(np.uint8)
    
def apply_filter(image,filter_type = "gaussian",ksize=5):

    if filter_type =="gaussian":
        return cv2.GaussianBlur(image,(ksize,ksize),0)
    
    elif filter_type == "median":
        return cv2.medianBlur(image,ksize)

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("no image found goodbye")
        return
    print("select an option:")
    print("Sobel edge detection")
    print("Canny edge detection")
    print("Laplacian edge detection")
    print("Gaussian smoothening")
    print("Median filtering")
    print("exit")

    while True:
        choice = input("enter your choice 1-6=")

        if choice == "1":
            ksize = int(input("Enter kernal size for sobel(odd number):"))
            result = apply_edge_detection(image, method="sobel",ksize=ksize)
            display_image("Sobel edge detection",result)

        elif choice == "2":
            threshold1 = int(input("enter lower threshold for canny"))
            threshold2 = int(input("enter upper threshold for canny:"))
            result = apply_edge_detection(image,method="canny",threshold1=threshold1,threshold2=threshold2)
            display_image("canny edge detection",result)

        elif choice == "3":
            result = apply_edge_detection(image,method="laplacian")
            display_image("Laplacian edge detection",result)
        
        elif choice == "4":
            ksize = int(input("enter kernel number for gaussian smoothening(odd number):"))
            result =apply_filter(image,filter_type="gaussian",ksize=ksize)
            display_image("gaussian smoothed image",result)

        elif choice == "5":
            ksize = int(input("Enter kernal size for median filtering(odd number):"))
            result = apply_filter(image,filter_type="median",ksize=ksize)
            display_image("median filtered image",result)
        
        elif choice == "6":
            print("exiting..................")
            break
        
        else:
            print("invalid choice.please select between 1 and 6")

interactive_edge_detection('pop.png')