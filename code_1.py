from PIL import Image
import os

# Paths
input_folder = 'D:\\zeyad\\unedited'  # Folder with your selected photos
output_folder = 'D:\\zeyad\\afteredit'  # Folder where edited photos will be saved
skin_image_path = 'D:\\zeyad\\skin.png'  # The transparent image to overlay

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the transparent image (skin)
skin = Image.open(skin_image_path).convert("RGBA")

# Iterate through all the images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add more formats if needed
        # Open each photo
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGBA")
        
        # Resize the skin to match the dimensions of the image
        skin_resized = skin.resize(img.size, Image.Resampling.LANCZOS)
        
        # Overlay the skin on the image
        combined = Image.alpha_composite(img, skin_resized)
        
        # Save the edited image in the output folder
        output_path = os.path.join(output_folder, filename)
        combined.save(output_path, "PNG")  # Save as PNG to preserve transparency if needed

        print(f"Saved {filename} with the overlay applied.")
