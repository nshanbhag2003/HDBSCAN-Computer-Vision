import numpy as np
from PIL import Image
import sys

def deconvolute_image_to_csv(input_image_path):
    """
    Reads a PNG image from input_image_path and deconvolutes it into three matrices (R, G, B).
    Saves each channel separately as R.csv, G.csv, and B.csv.
    """
    # Open image and ensure it's in RGB mode
    image = Image.open(input_image_path).convert('RGB')

    # Convert the image to a NumPy array
    img_array = np.array(image)
    # img_array has shape: (height, width, 3)

    # Separate the array into R, G, B
    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]

    # Save each channel to CSV
    np.savetxt("R.csv", R, fmt='%d', delimiter=",")
    np.savetxt("G.csv", G, fmt='%d', delimiter=",")
    np.savetxt("B.csv", B, fmt='%d', delimiter=",")

    print("Successfully saved R.csv, G.csv, and B.csv")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python deconvolute_image.py <input_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    deconvolute_image_to_csv(input_path)