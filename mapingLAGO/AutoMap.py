import sys,os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

################ ignorar algun estado on,soon,uc desde el argumento ##
# uprunning, ongoing, planned, suspended, cancelled
# suspended and cancelled ignored by default
ignore=[0,0,0,1,1]
for j in range(0,len(sys.argv)):
  if sys.argv[j]=='-uprunning':
     ignore[0]=1
  if sys.argv[j]=='-ongoing':
    ignore[1]=1
  if sys.argv[j]=='-planned':
    ignore[2]=1
  if sys.argv[j]=='-suspended':
    ignore[3]=0
  if sys.argv[j]=='-cancelled':
    ignore[4]=0

ig=ignore[0]+ignore[1]+ignore[2]+ignore[3]+ignore[4]

if ig==5:
  sys.exit("ERROR--IGNORANDO TODO!!!")
  
##################### define el marker y color segun el estado #######

def estatus(x):
  status=(0, 0)
  if x == 'uprunning':
    status=('^','#0033CC')
  elif x == 'ongoing':
    status=('s','#FF8C00')
  elif x == 'planned':
    status=('o','#CC0000')
  elif x == 'suspended':
    status=('-','#CCCC00')
  elif x == 'cancelled':
    status=('x','#CCCCCC')
  else:
    print (x)
    sys.exit("ERROR--ESTAUS DE SITIO NO VALIDO!!!")
  return status

################### ordena el archivo de datos por latitud#######

os.system('python3 sorteador.py '+sys.argv[1]+' 2 > misdatos.dat')
files=open('misdatos.dat')



#### genera mapa basico  #################################################
# map = Basemap(projection='cyl',llcrnrlat=-84,urcrnrlat=33.56,llcrnrlon=-118.25,urcrnrlon=-33.56,resolution='l')
lowerleftlat=-75
lowerleftlon=-110
upperrightlat=+55
upperrightlon=+20

map = Basemap(
  projection='cyl',
  llcrnrlat=lowerleftlat,
  llcrnrlon=lowerleftlon,
  urcrnrlat=upperrightlat,
  urcrnrlon=upperrightlon,
  resolution='l'
)
plt.figure(figsize=(13,18))

map.drawcoastlines(linewidth=.5)
map.drawcountries(linewidth=.5)
map.shadedrelief()
parallels = np.arange(-90.,50,10)
map.drawparallels(parallels,labels=[False,True,True,False])
#map.drawmapboundary(fill_color = 'aqua')
   
######################### grafica puntos sobre el mapa#############
lat = []
lon = []
yaux=0
yaux2=0
xaux=0
xaux2=0
x=0
y=0
cont=0
def crosletras(y,yaux,x,xaux,lengo,i):
  salida=[0,0]
  xo=0
  yo=0

  if abs(x-xaux)<8 and abs(y-yaux)<5:
    #salida[0]=x-3-(2*i/10)
    salida[0]=x-3-(1.5*i/10)+((abs(x-xaux)/(x-xaux))*(2-abs(x-xaux)))
  else:
    salida[0]=x-3-(2*i/10)
  if abs(y-yaux)<5:
    salida[1]=y+(5-abs(y-yaux)-2)
  if abs(y-yaux)>5:
    salida[1]=y-1
  return salida

for line in files:
  row = line.split(',')
  if ig>0:
    if ignore[0]>0 and row[4]=='uprunning': #ignora on
      continue
    if ignore[1]>0 and row[4]=='ongoing':#ignora ongoing
      continue
    if ignore[2]>0 and row[4]=='planned': #ingnora uc
      continue
    if ignore[3]>0 and row[4]=='suspended':#ignora suspended
      continue
    if ignore[4]>0 and row[4]=='cancelled':#ignora cancelled
      continue
  if row[0][0] == '#':
    continue
  cont += 1
  lat = float(row[2])
  lon = float(row[3])
  tatus=estatus(row[4]) # determina color y marker segun estatus
  x, y = map(lon, lat)

  map.scatter(
    x,
    y,
    marker=tatus[0],
    facecolor=tatus[1][0:7],
    s=150,
    zorder=10
  )
  # cornu=crosletras(y,yaux,x,xaux,len(row[1]),cont)
# markers
# grafica numeros impares a la izquierda del marker y pares a la derecha
  m=((-1)**(cont))
  plt.text(
    x + (m * 3) - ((0.5 + (cont / 10)) * m) + m * (cont / 10) - 1.3,
    y - 0.5,
    ('0' if cont < 10 else '') + str(cont),
    color='#000000',
    fontsize=10,
    zorder=15,
    fontfamily='monospace',
    fontweight='normal'
  )

# Leyenda
  # plt.text(-117,13-(2.6*cont),str(cont)+' = '+row[0]+' ('+str(int(float(row[1])))+' m)',color='w',fontsize=17,zorder=10, fontweight='bold')#grafica la leyenda que numero-lugar en blanco a la derecha
  plt.text(
    -30.0 , 
    +25.0 - (2.9 * cont), 
    ('0' if cont < 10 else '') + str(cont) + '. ' + row[0] + ' ('+str(int(float(row[1])))+' m)', 
    zorder=10, 
    color='#ffffff', 
    fontsize=15, 
    fontfamily='monospace',
    fontweight='bold'
  )


##################### genera etiquetas para la leyenda superior sobre los puntos##############################
xi=23
yi=23
fs=150
xi,yi=map(lon,lat)
if ignore[0]==0:
  plt.scatter(xi, yi, marker='^', s=fs, color='#0033CC', label='LAGO Site')
if ignore[2]==0:
  plt.scatter(xi, yi, marker='s', s=fs, color='#FF8C00', label='Deploying')
if ignore[1]==0:
  plt.scatter(xi, yi, marker='o', s=fs, color='#CC0000', label='Planned')
if ignore[3]==0:
  plt.scatter(xi, yi, marker='x', s=fs, color='#CCCC00', label='Suspended')
if ignore[4]==0:
  plt.scatter(xi, yi, marker='-', s=fs, color='#CCCCCC', label='Cancelled')
lg = plt.legend(loc='upper left', fontsize=20, scatterpoints=1)
lg.get_frame().set_alpha(.6) # A little transparency

os.system("rm misdatos.dat")
plt.savefig('lagoplano.png',dpi=300,bbox_inches='tight', pad_inches = 0)