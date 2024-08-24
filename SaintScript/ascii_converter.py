import numpy as np
from PIL import Image, ImageFilter, ImageOps

alphabet = {
    "cyrillic": "тгГузчксэлхУТяоьКнпъРЧциарПеЛСдмЗХЦЬжАЕвйёОыЭбИНЁюБЪЯФшЙщДВШфЫЩЖЮМ",
    "ascii": " .:-=+*#%@",
    "mkd-small": ".:тјгуѓчзскхлѕќопнџцираедмжвбњљшф"
}


def img_to_ascii(image_path, type_char="cyrillic", apply_blur=False, edge_detection=False, adaptive_threshold=False):
    try:
        # Load image and convert to grayscale
        image = Image.open(image_path).convert('L')
        print(image.size)
        # image = Image.open(image_path).resize((90, 60)).convert('L')
        # print(image.size)

        # Apply Gaussian Blur
        if apply_blur:
            image = image.filter(ImageFilter.GaussianBlur(radius=2))

        # Apply edge detection
        if edge_detection:
            image = image.filter(ImageFilter.FIND_EDGES)

        # Apply adaptive thresholding
        if adaptive_threshold:
            image = ImageOps.invert(image)  # Invert the image
            image = image.filter(ImageFilter.MedianFilter(size=3))
            image = ImageOps.autocontrast(image)

        # Select the character set
        chars = alphabet[type_char]

        # Normalize image data to map to the length of chars
        pixels = np.array(image)
        normalized_pixels = (pixels / 255.0) * (len(chars) - 1)
        normalized_pixels = normalized_pixels.astype(int)

        # Create ASCII art
        ascii_art = []
        for row in normalized_pixels:
            line = ''.join([chars[pixel] for pixel in row])
            ascii_art.append(line)

        ascii_art_str = '\n'.join(ascii_art)

        print(ascii_art.__len__())

        return ascii_art_str

    except Exception as e:
        return str(e)
