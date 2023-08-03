from PIL import Image
import glob
import os

# Directory containing the JPEG images
img_dir = "C:\\temp\\dozownik"

# Get the file paths and sort by modification time
file_list = glob.glob(os.path.join(img_dir, '*.jpg'))
file_list.sort(key=os.path.getmtime)

# Define the size to resize images
#size = (500, 500)  # Change this to the size you want

# Create a list to hold the image objects
img_list = []

for filename in file_list:
    img = Image.open(filename)
#    img = img.resize(size, Image.ANTIALIAS)  # Resize the image
    img_list.append(img)

output_path = os.path.join(img_dir, '360_output.gif')
# Save the images as a GIF
img_list[0].save(output_path, save_all=True, append_images=img_list[1:], optimize=False, duration=40, loop=0)
