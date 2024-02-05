# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# jerry

from PIL import Image
import os

def color_jerry():
# navigate to supplements folder and open the image
    pathname = os.path.join("hw4_supplements","berry.png")
    img = Image.open(pathname)
    rgb_vals = list(img.getdata()) # a list of rgb values
# your code goes here
    for i in range(len(rgb_vals)):
        if rgb_vals[i][2] >= 120 and rgb_vals[i][1] <= 100:
            rgb_vals[i] = (192,129,41)
# create a new image using the new RGB values
    img.putdata(rgb_vals)
    img.show()

color_jerry()
