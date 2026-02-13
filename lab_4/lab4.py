import arcpy


# Set workspace
arcpy.env.workspace = r'C:\Users\yidu\GISProg\lab4\codes_env'

# Paths
folder_path = r'C:\Users\yidu\GISProg\lab4'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name

# Create File Geodatabase
arcpy.CreateFileGDB_management(folder_path, gdb_name)

# CSV to XY points
csv_path = r'C:\Users\yidu\GISProg\lab4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path,'X','Y',garage_layer_name)

# Export points to GDB
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer,gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# Open campus gdb, copy building feature to our gdb
campus = r'C:\Users\yidu\GISProg\lab4\Campus.gdb'
buildings_campus = campus + '\\Structures'
buildings = gdb_path + '\\Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points,gdb_path + '\Garage_Points_reprojected', spatial_ref)

# buffer the garage
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

# Intersect the buffer with buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection','ALL')
arcpy.TableToTable_conversion( gdb_path + '\Garage_Building_Intersection.dbf', r'C:\Users\yidu\GISProg\lab4','nearbyBuildings.csv')

