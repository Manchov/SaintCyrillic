from PIL import Image, ImageDraw, ImageFont
import numpy as np
import sys

# Define Cyrillic characters
cyrillic_chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
mkd_chars = 'љњертѕуиопшѓасдфгхјклчќжзџцвбнм'

# Define font and image size
font_size = 20
font_path = "arial.ttf"  # Ensure the path to a TTF font that supports Cyrillic
font = ImageFont.truetype(font_path, font_size)
image_size = (font_size, font_size)


# Function to calculate "ink" density of a character
def calculate_density(char):
    # Create an image with white background
    image = Image.new('L', image_size, 255)
    draw = ImageDraw.Draw(image)
    # Draw the character on the image
    draw.text((0, 0), char, font=font, fill=0)
    # Convert image to numpy array and calculate density
    pixel_data = np.array(image)
    ink_density = np.mean(pixel_data < 128)  # proportion of dark pixels
    return ink_density


# Calculate densities for all characters
densities = [(char, calculate_density(char)) for char in mkd_chars]

# Sort characters by density
sorted_chars = sorted(densities, key=lambda x: x[1])

# Print sorted characters
sorted_chars_str = ''.join([char for char, _ in sorted_chars])

# Ensure the console output is in cp855
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='cp855', buffering=1)

print("Characters sorted by 'ink' density:", sorted_chars_str)

# Optionally, save sorted characters to a file with UTF-8 encoding
with open('sorted_cyrillic_chars.txt', 'w', encoding='utf-8') as f:
    f.write(sorted_chars_str)
