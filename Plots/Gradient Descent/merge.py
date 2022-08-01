import os
from PIL import Image

os.chdir(os.path.dirname(os.path.realpath(__file__)))

img_01 = Image.open("output/hyperplane-2D.png")
img_02 = Image.open("output/hyperplane-3D.png")

img_02 = img_02.resize((int(img_02.size[0]/img_02.size[1]*img_01.size[1]), img_01.size[1]))

new_im = Image.new('RGB', (img_01.size[0] + 10 + img_02.size[0],img_01.size[1]), (255,255,255))

new_im.paste(img_01, (0,0))
new_im.paste(img_02, (img_01.size[0] + 10,0))

new_im.save("output/hyperplanes.png", "PNG")
new_im.show()