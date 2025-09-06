# Advanced Background Removal for Images

This project provides a Python-based solution to automatically remove and replace backgrounds from images using the **Rembg** library, along with resizing and batch processing capabilities. It is designed to handle large sets of images efficiently and supports advanced options like alpha matte and custom background colors.

---

## Features

- **Automatic background removal** using the state-of-the-art `rembg` library.
- **Supports alpha matte** and custom background colors.
- **Batch processing**: Automatically processes all images in a folder.
- **Resizes images** to a specified dimension for consistent output.
- Handles **common image formats**: `.jpg`, `.jpeg`, `.png`.
- **Error handling** for robust processing of large image sets.

---

## Requirements

- Python 3.8+
- OpenCV (`cv2`)
- Numpy (`numpy`)
- Rembg (`rembg`)

Install dependencies using pip:

```bash
pip install opencv-python numpy rembg
