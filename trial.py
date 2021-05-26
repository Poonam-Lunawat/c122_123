# importing image class from PIL package
from PIL import Image
  
# creating image object
img = Image.open("bharadwaj.jpg")
  
# using convert method for img1
#If you have an L mode image, that means it is a single channel image - normally interpreted as greyscale. 
# The L means that is just stores the Luminance. It is very compact, but only stores a greyscale, not colour.
# P mode RGB value in 1 pixel
#l mode only luminance values...gray scale 
img1 = img.convert("P")
img1.show()
  
# using convert method for img2
# img2 = img.convert("1")
# img2.show()