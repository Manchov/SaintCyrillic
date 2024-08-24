from SaintScript.ascii_converter import img_to_ascii
from SaintScript.resizer import img_resize


def convert(image_path, type_char="cyrillic"):
    if type == "cyrillic":
        return img_to_ascii(image_path, type_char,apply_blur=False,edge_detection=False,adaptive_threshold=False)


def resize(img, screen_width, screen_height):
    return img_resize(img, screen_width, screen_height)
