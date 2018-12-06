
import fiona
import rasterio
import rasterio.mask

with fiona.open("/media/khoi/Data/Building/Data/IMG2/BOX/48/Kanataka_0048.shp", "r") as shapefile:
    features = [feature["geometry"] for feature in shapefile]
# print(features[0],"\n",features[1])
with rasterio.open("/media/khoi/Data/Building/Data/IMG2/Kanataka_0048.tif") as src:
    for i in range(len(features)):
        print(i,"-------------")  
        out_image, out_transform = rasterio.mask.mask(src, [features[i]],crop=True)
        out_meta = src.meta.copy()

        out_meta.update({"driver": "GTiff",
                        "height": out_image.shape[1],
                        "width": out_image.shape[2],
                        "transform": out_transform})
        a = str(i)
        with rasterio.open("/media/khoi/Data/Building/Data/IMG2/cut/48/Kanataka_0048_cut_"+a+".tif", "w", **out_meta) as dest:
            dest.write(out_image)