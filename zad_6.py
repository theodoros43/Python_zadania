#!/usr/bin/python3

from PIL import Image
import os

im1 = Image.new("RGB", (512,512))
im2 = Image.new("RGB", (512,512))
im3 = Image.new("RGB", (512,512))
im4 = Image.new("RGB", (512,512))

im1.save('1.jpg', "JPEG")
im2.save('2.jpg', "JPEG")
im3.save('3.jpg', "JPEG")
im4.save('4.jpg', "JPEG")

im = Image.open("1.jpg")
path = os.getcwd()
im.save("1.png","PNG")
os.unlink(path + "/1.jpg")
