from pathlib import Path
import json
import numpy as np
import geopandas as gpd
import rasterio
from rasterio.transform import from_origin
from scipy.ndimage import gaussian_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from pyproj import Transformer

P=Path(__file__).resolve().parent
with rasterio.open(P/'mdt02_700_4736.asc') as ds:
 print('datos',ds.bounds,ds.res,ds.nodata,ds.crs)
 a=ds.read(1).astype('float32'); a[a==ds.nodata]=np.nan
 print('cobertura valida',np.isfinite(a).mean())
 b=ds.bounds; tf=ds.transform
s=gpd.read_file(P/'WatercourseLink.gml').to_crs(25829)
items=[('Norte','6800262','#00e7ff'),('Sur','6806167','#ffba23'),('Tramo común','6800261','#ff46d7')]
fig,axs=plt.subplots(2,2,figsize=(16,12),layout='constrained')
clip=(slice(50,500),slice(350,1000));z=a[clip];x1=b.left+350*2;x2=b.right;y1=b.top-500*2;y2=b.top-50*2
print('valid clip',np.isfinite(z).mean(),'zrange',np.nanmin(z),np.nanmax(z))
fill=np.nan_to_num(z,nan=float(np.nanmedian(z)))
relief=fill-gaussian_filter(fill,6)
shade=LightSource(azdeg=315,altdeg=40).hillshade(fill,dx=2,dy=2)
axs[0,0].imshow(shade,extent=[x1,x2,y1,y2],cmap='gray',origin='upper');axs[0,0].set_title('Relieve sombreado, MDT02')
axs[0,1].imshow(relief,extent=[x1,x2,y1,y2],cmap='RdBu_r',vmin=-5,vmax=5,origin='upper');axs[0,1].set_title('Relieve local respecto a entorno (rojo alto, azul bajo)')
axs[1,0].imshow(plt.imread(P/'AMS_1956-1957.jpg'),extent=[700700,702000,4735000,4735900]);axs[1,0].set_title('Vuelo 1956–1957')
axis=axs[1,1]; results=[]
for name,suffix,color in items:
 line=s[s.gml_id.str.endswith(suffix)].iloc[0].geometry
 dists=np.arange(0,line.length,2);pts=[line.interpolate(float(d)) for d in dists]
 rr,cc=rasterio.transform.rowcol(tf,[p.x for p in pts],[p.y for p in pts]);rr=np.asarray(rr);cc=np.asarray(cc);zz=a[rr,cc]
 axis.plot(dists,zz,c=color if name!='Norte' else '#008cab',label=name)
 win=[]
 for i in range(len(pts)-10):
  j=i+10
  if np.isfinite(zz[i]) and np.isfinite(zz[j]):win.append((float(zz[i]-zz[j]),i))
 win.sort(reverse=True);peaks=[]
 for delta,i in win:
  if all(abs(i-q['idx'])>15 for q in peaks):
   lon,lat=Transformer.from_crs(25829,4326,always_xy=True).transform(pts[i].x,pts[i].y)
   peaks.append({'idx':i,'dist_m':float(dists[i]),'descenso_m_en_20m':round(delta,2),'lat':round(lat,6),'lon':round(lon,6),'elevacion_inicio':round(float(zz[i]),2),'elevacion_final':round(float(zz[i+10]),2)})
   if len(peaks)>=4:break
 results.append({'tramo':name,'distancia_m':round(line.length,1),'elev_inicio':round(float(zz[0]),2),'elev_final':round(float(zz[-1]),2),'valid_pct':round(float(np.isfinite(zz).mean()*100),1),'sectores_mayor_desnivel':peaks})
 for ax in axs.flat[:3]:
  X,Y=line.xy;ax.plot(X,Y,c=color,lw=1.7,label=name)
axis.set_title('Perfil sobre la línea cartográfica actual');axis.set_xlabel('Distancia desde cabecera cartografiada, m');axis.set_ylabel('Altitud aproximada, m');axis.grid(alpha=.25);axis.legend()
for ax in axs.flat[:3]:
 ax.scatter([701843.56,701494.5],[4735415.84,4735508.23],c='white',edgecolors='black',s=25);ax.set_xlim(x1,x2);ax.set_ylim(y1,y2);ax.set_aspect('equal');ax.ticklabel_format(style='plain',useOffset=False);ax.tick_params(labelsize=7)
axs[0,0].legend(loc='lower left',fontsize=8)
fig.suptitle('Cauce junto al paraje Escandal: análisis exploratorio LiDAR 2 m',fontsize=16)
fig.text(.02,.002,'Líneas: cauces actuales del IGN, no cauces históricos; posición y perfiles aproximados. El modelo no identifica agua ni pozas. Fuente: MDT02 PNOA2, JCyL / IGN / ITACyL (2017–2021), bloque NW 700_4736, pendiente control de calidad.',fontsize=8)
fig.savefig(P/'escandal_lidar2_y_vuelo1956.png',dpi=160)
(P/'lidar2_perfiles.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf8')
print(json.dumps(results,indent=2,ensure_ascii=False))
