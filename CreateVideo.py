import os
import cv2

# Set path for the Images folder
path = "Images/"

# Create empty list for images
images = []

# Check each file in the folder
for file in os.listdir(path):

    # Separate the name and extension from a file name
    name, ext = os.path.splitext(file)

    # Check if the extension of the file matches with the image extension
    if ext in [".png", ".jpg", ".jpeg"]:

        # Create a variable file_name by concatenating the path and file name
        file_name = os.path.join(path, file)

        # Add each file in the images list
        images.append(file_name)

# Get number of images
count = len(images)

# Read the first image from the images list
frame = cv2.imread(images[0])

# Get frame dimensions
height, width, channels = frame.shape

# Set video size
size = (width, height)

# Create VideoWriter object
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Loop through images and add to VideoWriter
for i in range(0, count):

    # Read image using cv2.imread()
    img = cv2.imread(images[i])

    # Add image to VideoWriter
    out.write(img)

# Release VideoWriter and print completion message
out.release()
print("Done!")
