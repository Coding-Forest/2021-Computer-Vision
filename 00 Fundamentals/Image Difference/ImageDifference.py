# References: Jie Jenn (2019) How to compare two images and display the differences using Python (Hint: Pillow) https://www.youtube.com/watch?v=fUfvBnREBFc&ab_channel=JieJenn
# Image from Kelly Lacy https://www.pexels.com/@km-l-1179532/

from PIL import Image, ImageChops

img1 = Image.open("difference/vlcsnap-00005.png")
img2 = Image.open("difference/vlcsnap-00006.png")

diff = ImageChops.difference(img1, img2)

if (diff.getbbox()):
    diff.show()                          # shows the image.
    diff.save("difference/diff1.png")    # save the difference imge object.
