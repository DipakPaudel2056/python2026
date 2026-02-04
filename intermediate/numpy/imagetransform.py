# here we will transform an image using numpy
import numpy as np
from PIL import Image

im = Image.open("image_3.jpg")
print(im.size)
# Let's convert the image to a numpy array
im_array = np.array(im)
print("Image array shape:", im_array.shape)
# Now let's perform some transformations
# 1. Rotate the image by 90 degrees
rotated_im_array = np.rot90(im_array)
# 2. Flip the image horizontally
flipped_im_array = np.fliplr(im_array)
# 3. Convert the image to grayscale
if im_array.ndim == 3 and im_array.shape[2] == 3:
    grayscale_im_array = np.dot(im_array[..., :3], [0.2989, 0.5870, 0.1140])
else:
    grayscale_im_array = im_array  # already grayscale
# Convert back to images and save
rotated_im = Image.fromarray(rotated_im_array)
rotated_im.save("rotated_image.jpg")    
flipped_im = Image.fromarray(flipped_im_array)
flipped_im.save("flipped_image.jpg")
grayscale_im = Image.fromarray(grayscale_im_array.astype(np.uint8))
grayscale_im.save("grayscale_image.jpg")