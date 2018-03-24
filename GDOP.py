#########################
# Resnick Xing
# 2018/3/24
# github:@DeepTrial
#########################

import glob,math
from calCenter import calCenter



def imagelist(path,type):
	imagelist=glob.glob(path+'*.'+type)
	return imagelist

def calGDOP(gtList,predPath,predType):
	'''

	:param gtList: groundtruth image path list
	:param predPath: prediction image path
	:param predType: prediction image type
	:return: GDOP result
	'''
	dx=0.0
	dy=0.0
	Nimgs=len(gtList)
	for gtImagePath in gtList:
		predImagePath=predPath+((gtImagePath.split('\\')[-1]).split('.')[0])+'.'+predType
		#print(predImagePath)
		cx,cy=calCenter(gtImagePath)
		cx_,cy_=calCenter(predImagePath)
		dx=(cx-cx_)*(cx-cx_)
		dy=(cy-cy_)*(cy-cy_)
	dx=float(dx/Nimgs)
	dy=float(dy/Nimgs)
	resultGDOP=math.sqrt(dx+dy)
	return resultGDOP




if __name__=="__main__":
	groundtruth=".\\groundtruth\\"
	gtType="tif"
	gtList=imagelist(groundtruth,gtType)

	prediction=".\\prediction\\"
	predType="bmp"

	result=calGDOP(gtList,prediction,predType)
	print("----------------------------------")
	print("total images: ",len(gtList))
	print("the Geometric Dilution Precision on your dataset is: ",result)



