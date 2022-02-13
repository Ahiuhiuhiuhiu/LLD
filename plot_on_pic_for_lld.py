#common used python libraries
import numpy as np
import json
from urllib.request import urlopen
import requests
from scipy.misc import imread
from scipy.ndimage import imread
from PIL import Image

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
from io import StringIO
import glob
from scipy import ndimage, misc
import skimage
from sklearn.utils import shuffle
import random
import time
import timeout_decorator

import io
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import urllib
 
from os.path import join as pjoin
import matplotlib.pyplot as plt
import numpy as np
import json
import cv2
from skimage import io

import pandas
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import urllib


import requests
from IPython.core.display import display, HTML
import requests
import urllib.request
import csv
import json
import numpy as np
from sklearn import svm

from PIL import Image
import requests
from io import BytesIO
import os

%matplotlib inline

data = np.load('xxx.npy')

data_list = []
for i in data:
    data_list.append(i)

for uuid in data_list:
    try:
        pic_url = 'http://pic_url'.jpg'

        print (i)
        print (pic_url)
        print (xxx[i])

        center_lane_left_line_point_x_list = []
        center_lane_left_line_point_y_list = []
        
        center_lane_right_line_point_x_list = []
        center_lane_right_line_point_y_list = []
        
        
        
        left_lane_left_line_point_x_list = []
        left_lane_left_line_point_y_list = []
        
        left_lane_right_line_point_x_list = []
        left_lane_right_line_point_y_list = []
        
        
        right_lane_left_line_point_x_list = []
        right_lane_left_line_point_y_list = []
        
        right_lane_right_line_point_x_list = []
        right_lane_right_line_point_y_list = []
        
        
        for lane in data[0]['lanes']:
            if lane['position'] == 'center':
                for point in lane['left_line']['points']:
                    center_lane_left_line_point_x_list.append(int(point['x']))
                    center_lane_left_line_point_y_list.append(int(point['y']))
        
                for point in lane['right_line']['points']:
                    center_lane_right_line_point_x_list.append(int(point['x']))
                    center_lane_right_line_point_y_list.append(int(point['y']))
                    
            elif lane['position'] == 'left':
                for point in lane['left_line']['points']:
                    left_lane_left_line_point_x_list.append(int(point['x']))
                    left_lane_left_line_point_y_list.append(int(point['y']))
        
                for point in lane['right_line']['points']:
                    left_lane_right_line_point_x_list.append(int(point['x']))
                    left_lane_right_line_point_y_list.append(int(point['y']))
                    
            elif lane['position'] == 'right':
                for point in lane['left_line']['points']:
                    right_lane_left_line_point_x_list.append(int(point['x']))
                    right_lane_left_line_point_y_list.append(int(point['y']))
        
                for point in lane['right_line']['points']:
                    right_lane_right_line_point_x_list.append(int(point['x']))
                    right_lane_right_line_point_y_list.append(int(point['y']))
                    
            


        center_left = len(center_lane_left_line_point_x_list)    
        center_right = len(center_lane_right_line_point_x_list)
        
        
        left_left = len(left_lane_left_line_point_x_list)
        left_right = len(left_lane_right_line_point_y_list)
        
        right_left = len(right_lane_left_line_point_x_list)
        right_right = len(right_lane_right_line_point_y_list)
        

        tmp_image = io.imread(pic_url)
            

        for i in range(0,center_left):
            center_left_x = center_lane_left_line_point_x_list[i]
            center_left_y = center_lane_left_line_point_y_list[i]

            cv2.circle(tmp_image,(center_left_x,center_left_y), 8, (0,0,255), -1)
        
        for i in range(0,center_right):
            center_right_x = center_lane_right_line_point_x_list[i]
            center_right_y = center_lane_right_line_point_y_list[i]

            cv2.circle(tmp_image,(center_right_x,center_right_y), 8, (255,0,0), -1)
            
        for i in range(0,left_left):
            left_left_x = left_lane_left_line_point_x_list[i]
            left_left_y = left_lane_left_line_point_y_list[i]

            cv2.circle(tmp_image,(left_left_x,left_left_y), 8, (0,255,0), -1)
            
        for i in range(0,left_right):
            left_right_x = left_lane_right_line_point_x_list[i]
            left_right_y = left_lane_right_line_point_y_list[i]

            cv2.circle(tmp_image,(left_right_x,left_right_y), 8, (0,0,255), -1)
            
        for i in range(0,right_left):
            right_left_x = right_lane_left_line_point_x_list[i]
            right_left_y = right_lane_left_line_point_y_list[i]

            cv2.circle(tmp_image,(right_left_x,right_left_y), 8, (255,0,0), -1)
            
        for i in range(0,right_right):
            right_right_x = right_lane_right_line_point_x_list[i]
            right_right_y = right_lane_right_line_point_y_list[i]

            cv2.circle(tmp_image,(right_right_x,right_right_y), 8, (0,128,128), -1)
            
            
        
        plt.figure(num=None, figsize=(8, 6), dpi=120, facecolor='w', edgecolor='k')   
        plt.imshow(tmp_image)
        plt.show()

    
    except Exception as e:
        json_url = 'http://json_url/' + xxx[i]
        url = 'http://status_url/' +xxx[i]

        #uulist.append(uuid_list[i])

        data = json.load(urlopen(json_url))
        data1 = json.load(urlopen(url))

        prefix = data1[0]["prefix"]

        pic_url = 'http://json_url/' + prefix + '/' + xxx[i] + '.jpg'
        print (xxx[i])
        print (pic_url)
        print(e)
    
    
    plt.show()
    