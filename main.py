import Pet
import asyncio

import io
from PIL import Image
from PIL import ImageDraw

img = Image.open("stone.png", mode='r')  

img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()

Pet.get_pet(img_byte_arr)

