# Image Resizer
from PIL import Image
import os
size = (300, 300)
for img in os.listdir("images"):
    if img.endswith(("png", "jpg", "jpeg")):
        Image.open(f"images/{img}").resize(size).save(f"resized/{img}")
