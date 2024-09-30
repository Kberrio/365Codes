import cv2
import numpy as np

def apply_filters(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply edge detection
    edges = cv2.Canny(blurred, 100, 200)

    # Apply threshold
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Apply dilation and erosion
    kernel = np.ones((5,5), np.uint8)
    dilation = cv2.dilate(threshold, kernel, iterations=1)
    erosion = cv2.erode(threshold, kernel, iterations=1)

    # Apply histogram equalization
    equ = cv2.equalizeHist(gray)

    # Display results
    cv2.imshow('Original', img)
    cv2.imshow('Grayscale', gray)
    cv2.imshow('Blurred', blurred)
    cv2.imshow('Edges', edges)
    cv2.imshow('Threshold', threshold)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Equalized', equ)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_filters('path_to_your_image.jpg')