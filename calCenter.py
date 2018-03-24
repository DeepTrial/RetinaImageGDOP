#########################
# Resnick Xing
# 2018/3/24
# github:@DeepTrial
#########################

import cv2
import numpy as np


#In this function,center coordinate is the average of white label
#because the label is circle,please choose your own way to calculate the center coordinate

def calCenter(image_path):
	image=cv2.imread(image_path,0)
	od_coord=np.where(image==np.max(image))
	centerx=np.mean(od_coord[0])
	centery=np.mean(od_coord[1])
	return centerx,centery