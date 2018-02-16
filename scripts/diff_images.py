
from PIL import Image, ImageChops

def diff_images(img1, img2, d1, d2):

  diff1 = ImageChops.subtract(img1,img2)
  diff2 = ImageChops.subtract(img2,img1)

  diff1.save(d1)
  diff2.save(d2)

if __name__ == '__main__':
  diff_images()
