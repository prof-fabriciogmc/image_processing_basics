##
# A simple image signature example
#
# Author: Fabrício G. M. de Carvalho, Ph.D.
##


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from model import img_signature, distance


ref_img_1 = mpimg.imread('data/ref_circunference.bmp')
ref_img_2 = mpimg.imread('data/ref_square.bmp')
unknown_img = mpimg.imread('data/unknown_image_3.bmp')

ref_img_1_prop = {'class': 'circunference', 'rows': len(ref_img_1), 'columns': len(ref_img_1[0])}
ref_img_2_prop = {'class': 'square', 'rows': len(ref_img_2), 'columns': len(ref_img_2[0])}
unknown_img_prop = {'class': 'unknown', 'rows': len(unknown_img), 'columns': len(unknown_img[0])}

## Compute image horizontal signatures:
ref_img_1_prop['h_signature'] = img_signature(ref_img_1,'h')
ref_img_2_prop['h_signature'] = img_signature(ref_img_2,'h')
unknown_img_prop['h_signature'] = img_signature(unknown_img,'h')


plt.figure(1)
plt.plot(ref_img_1_prop['h_signature'])
plt.title('Circunference')
plt.figure(2)
plt.plot(ref_img_2_prop['h_signature'])
plt.title('Square')

distance_img_1_to_unknown = distance(ref_img_1_prop['h_signature'], unknown_img_prop['h_signature'])
distance_img_2_to_unknown = distance(ref_img_2_prop['h_signature'], unknown_img_prop['h_signature'])

if distance_img_1_to_unknown < distance_img_2_to_unknown:
    unknown_img_prop['class'] = ref_img_1_prop['class']
elif distance_img_1_to_unknown >= distance_img_2_to_unknown:
    unknown_img_prop['class'] = ref_img_2_prop['class']
else:
    print('No classification problem...')

print("Final classification based on signature: " + unknown_img_prop['class'])

plt.figure(3)
plt.plot(unknown_img_prop['h_signature'])
plt.title(unknown_img_prop['class'])
plt.show()


