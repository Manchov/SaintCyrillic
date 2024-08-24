import numpy as np
from PIL import Image

def img_resize(file_path,screen_width,screen_height):
    with Image.open(file_path) as img:
        img_ratio = img.width / img.height
        screen_ratio = screen_width / screen_height

        # if img_ratio > screen_ratio:
        #     new_width = screen_width
        #     new_height = int(new_width / img_ratio)
        # else:
        #     new_height = screen_height
        #     new_width = int(new_height * img_ratio)

        new_width = screen_width
        new_height = int(new_width / img_ratio)

        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img.save(file_path)