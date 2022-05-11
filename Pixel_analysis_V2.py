from PIL import Image

image = Image.open(r"F:/test.jpg")
count = 0

# image.getdata() returns all the pixels in the image
for pixel in image.getdata():
    if pixel <= (255, 102, 102) and pixel >=(170, 0, 0):
        count += 1

print(count)
