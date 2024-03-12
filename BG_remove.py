import cv2
import numpy as np
from rembg import remove
import os
def remove_background_advanced(input_path, output_path, alpha_matte=False, background_color=(255, 255, 255)):
    with open(input_path, "rb") as input_file, open(output_path, "wb") as output_file:
        input_data = input_file.read()

        # Use advanced options
        output_data =remove(input_data, alpha_matte=alpha_matte, background_color=background_color)
        output_file.write(output_data)
        

# Get the list of all image files in the folder
folder_path = "Defective/"
image_files = [file for file in os.listdir(folder_path) if file.endswith((".jpg", ".jpeg", ".png"))]
i=0
# Process each image file
for image_file in image_files:
    input_path = os.path.join(folder_path, image_file)
    output_image = f"Pre_Defective/Pre_image_def_{i}.jpg"
    input = cv2.imread(input_path)
    remove_background_advanced(input_path, output_image, alpha_matte=True, background_color=(0, 0, 0))
    output = cv2.imread(output_image)
    image1 =cv2.resize(output, (250, 250), interpolation = cv2.INTER_LINEAR)
    cv2.imwrite(output_image, image1) 
    i+=1
    # Perform further operations on the output image
    # ...

# Note: Make sure to handle any exceptions that may occur during the processing of images.

