import os,sys
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

comand='python3 mapingLAGO/AutoMap.py '
comand2='python3 SitiosAlturas/plotalturas3.py '

for i in range(1, len(sys.argv)):
  comand+=sys.argv[i]+' '
  comand2+=sys.argv[i]+' '

print  ("generando mapa..... ")
os.system(comand) 
print  ("reduciendo mapa..... ")
os.system('convert lagoplano.png -scale 25% lagoplano_small.jpg')
# print ("\n\n\ngenerando curva de alturas... \n\n\n")
# os.system(comand2)

# fig = plt.figure()
# gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1.2],left=None,bottom=None,right=None,top=None,wspace=.005,hspace=.005)

# ax1=plt.subplot(gs[0])
# ax1.set_axis_off()
# img = mpimg.imread('lagoplano.png')
# lum_img = img[:,:,:]
# imgplot = plt.imshow(lum_img)

# ax2=plt.subplot(gs[1])
# ax2.set_axis_off()
# img2 = mpimg.imread('alturas3.png')
# lum_img2 = img2[:,:,:]
# imgplot2 = plt.imshow(lum_img2)
# plt.savefig("MAPAtodo.png",dpi=72,bbox_inches='tight', pad_inches = 0)