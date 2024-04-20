import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('person.png', cv2.IMREAD_GRAYSCALE)

# Thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract the largest contour
largest_contour = max(contours, key=cv2.contourArea)

# Extract coordinates of the contour points
pts = largest_contour.squeeze().tolist()
print(pts)
# Plot the points
x_coords = [pt[0] for pt in pts]
y_coords = [pt[1] for pt in pts]

plt.figure()
plt.plot(x_coords, y_coords, '.')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
