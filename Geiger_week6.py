import arcpy
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap 
import geopandas


#make selection based off year
hurricane_data = "hurricane"
wc = "year >= 2020 And year <= 2021"
hurricane_sel = arcpy.management.SelectLayerByAttribute(hurricane_data, "NEW_SELECTION", wc)

#convert selecton of fc to .shp
hurricane_shp = arcpy.conversion.FeatureClassToShapefile(hurricane_sel, r"C:\Users\dillongeiger\Desktop\Week6_Data")

# Lambert Conformal Conic map.
m = Basemap(merc)

# read shapefile.
hurricane_path = r"C:\Users\dillongeiger\Desktop\Week6_Data\hurricane.shp"
df = geopandas.read_file(hurricane_path)
df.plot()

# draw coastlines, meridians and parallels.
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')
plt.title('Hurricane Tracks Durring the Years 2020 - 2021')
plt.show()
