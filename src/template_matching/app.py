# Image matching example.
#
# Author: Fabrício G. M. de Carvalho, Ph.D.


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from model import match_template


template_img = mpimg.imread('data/template.png')
full_image = mpimg.imread('data/image.png')

template_prop = {'rows':len(template_img), 'columns':len(template_img[0])}
full_image_prop = {'rows':len(full_image), 'columns':len(full_image[0])}

answer = match_template(template_img, full_image)
print('Delta X: ' + str(answer['delta_x']))
print('Delta Y: ' + str(answer['delta_y']))

print('Program finished...')






