import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

hurricane_path = r"C:\Users\dillongeiger\Desktop\Week6_Data\hurricane.shp"
df = gpd.read_file(hurricane_path)
print(df)


##NotImplementedError: Multi-part geometries do not themselves provide the array interface##
