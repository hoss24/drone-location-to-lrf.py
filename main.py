from glob import glob
from os.path import join
from exifTool import exifTool
from lrfTool import lrfTool

file_extensions = ['**/*.jpg', '**/*.JPG']
tags = ["-GPSStatus", "-LRFStatus", "-GPSLatitude", "-LRFTargetLon", "-LRFTargetLat"]
# Use True to overwrite existing files, False to create backup copies
overwrite = True
ignore_warning = True
directory = input("""
Please input file directory by typing or dragging and dropping folder from Finder/File Explorer.
Tap Enter on keyboard to Run. 
Can leave input blank to run from current directory.
All folders and files within directory specified will be included
All files will be overwritten, edit overwrite value in main.py to create backup copies:""").strip()

exifTool = exifTool()
lrfTool = lrfTool()

image_files = set()
for ext in file_extensions:
    image_files.update(glob(join(directory, ext), recursive=True))

if not image_files:
    print(f"No files with extension {file_extensions} found in directory {directory}")

for file in image_files:
    file_tag_data = exifTool.extract_tag_data(tags=tags, file=file)
    image_lrf_data = lrfTool.get_lat_lon(file_tag_data)
    if image_lrf_data is not None:
        exifTool.replace_gps(file=file, coordinates=image_lrf_data,
                             overwrite_original=overwrite, ignore_warning=ignore_warning)
        print(f"{file} GPS Replaced with LRF: {image_lrf_data} \n")
    else:
        print(f'{file} Unable to replace GPS with LRF Data, confirm LRFStatus is "Normal" and (drone) GpsStatus is '
              f'"GPS" or "RTK"')

end = input("Process Completed. Press any key to continue.")
