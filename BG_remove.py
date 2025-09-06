import cv2
import numpy as np
from rembg import remove
import os

def remove_background_advanced(input_path, alpha_matte=False, background_color=(255, 255, 255)):
    """
    Remove background from an image using rembg with optional alpha matte and background color.

    Returns the processed image as a numpy array (BGR format).
    """
    try:
        with open(input_path, "rb") as f:
            input_data = f.read()
        # Remove background
        output_data = remove(input_data, alpha_matte=alpha_matte, background_color=background_color)
        # Convert bytes to numpy array
        nparr = np.frombuffer(output_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
        # If alpha channel exists, convert to BGR
        if img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return None

def process_images(input_folder="Defective/", output_folder="Pre_Defective/", resize_dim=(250, 250)):
    os.makedirs(output_folder, exist_ok=True)
    
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    
    for i, image_file in enumerate(image_files):
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, f"Pre_image_def_{i}.jpg")
        
        img = remove_background_advanced(input_path, alpha_matte=True, background_color=(0, 0, 0))
        if img is not None:
            resized_img = cv2.resize(img, resize_dim, interpolation=cv2.INTER_LINEAR)
            cv2.imwrite(output_path, resized_img)
            print(f"Processed {image_file} -> {output_path}")
        else:
            print(f"Skipping {image_file} due to processing error.")

if __name__ == "__main__":
    process_images()
