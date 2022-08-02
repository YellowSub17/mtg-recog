
import numpy as np


import matplotlib.pyplot as plt
plt.close('all')
import pytesseract as pyt
from PIL import Image
import time
import cv2
import os






CAM = cv2.VideoCapture(2)

def capture_and_save():

    result, cap = CAM.read()

    if result:
        cv2.imwrite(f'./data/{str(time.time()).split(".")[0]}.png', cap)
        cv2.imwrite(f'./data/{str(time.time()).split(".")[0]}_crop.png', cap[230:334, 215:789])
        cv2.imwrite('./data/tmp_crop.png', cap[230:334, 200:789])
        cv2.imwrite('./data/tmp.png', cap)
    else:
        print('Error: no result')









def read_im():
    for file in os.listdir('./data'):

        im = cv2.imread(f'./data/{file}')

        print(file)
        print(pyt.image_to_string(im))
        print()











# cam = cv2.VideoCapture(2)

# result, image = cam.read()


# im = Image.fromarray(image)

# if result:


    # cv2.imshow('x', image)
    # cv2.waitKey(0)

    # crop = image[200:350,200:700]

    # print(pyt.image_to_string(image,))
    # crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    # #gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video2


    
    # cv2.imshow('x', crop)
    # cv2.waitKey(0)


    # print(pyt.image_to_string(crop,))



# else:
    # print('no image detected')

if __name__=='__main__':

    # get_crop_indices()

    capture_and_save()


    read_im()
