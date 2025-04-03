import arcpy
from arcpy import env
env.workspace=r"C:\Users\abah035\Desktop\Lecture 7\Module7_Data\OTTAWA.gdb\Ottawadata"
print(arcpy.ListFeatureClasses())