import arcpy

#assign bands
source = r"C:\Users\yidu\GISProg\lab7"
band1 = arcpy.sa.Raster(source + r"\band1.tif")  #blue
band2 = arcpy.sa.Raster(source + r"\band2.tif")  #green
band3 = arcpy.sa.Raster(source + r"\band3.tif")  #red
band4 = arcpy.sa.Raster(source + r"\band4.tif")  #NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

#Hillshade
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + r"\DEM.tif", source + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

#Slope
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\DEM.tif", source + r"\output_Slop.tif", output_measurement, z_factor)
print("success!")