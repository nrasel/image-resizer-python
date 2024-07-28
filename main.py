import cv2

# Load the image
image = cv2.imread('download.jfif')

# Check if the image was loaded properly
if image is None:
    print("Error loading image")
    exit()

# Display original dimensions
original_dimensions = image.shape
print(f"Original Dimensions: {original_dimensions}")

# Set new dimensions
width = 500
height = 500
new_dimensions = (width, height)

# Resize the image
resized_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_AREA)

# Display resized dimensions
resized_dimensions = resized_image.shape
print(f"Resized Dimensions: {resized_dimensions}")

# Save the resized image
cv2.imwrite('resized_image.jpg', resized_image)

# Display both images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()