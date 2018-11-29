from osgeo import gdal
import numpy as np

def raster2array(rasterfn,number_band):
    # raster = gdal.Open(rasterfn)
    band = rasterfn.GetRasterBand(number_band)
    array = band.ReadAsArray()
    return array

filepath1 = r"E:\0_Data\Tree\Felcra_Kg_Wa_tiff\Train\tmp\region5_cut_img_crop_data_day\train\images\COCO_train2014_0_0074.tif"
filepath2 = r"E:\0_Data\Tree\Felcra_Kg_Wa_tiff\Train\tmp\region5_cut_img_crop_data_day\train\images\COCO_train2014_0_0010.tif"

raster1 = gdal.Open(filepath1)
raster2 = gdal.Open(filepath2)

band1 = raster2array(raster1,1)
band2 = raster2array(raster1,2)
band3 = raster2array(raster1,3)
band4 = raster2array(raster1,4)
band_1 = raster2array(raster2,1)
band_2 = raster2array(raster2,2)
band_3 = raster2array(raster2,3)
band_4 = raster2array(raster2,4)
print(band1.shape)
x = np.array([band1, band2, band3, band_1, band_2, band_3])
print(x.shape)

x1 = np.swapaxes(x,0,1)
img = np.swapaxes(x1,1,2)
# cách viết khác là chuyển x la doi tuong nhung code nayf loix  :D
img = (x.swapaxes(0,1)).swapaxes(1,2)
print(img.shape)







# print(img)#, band2, band3)
