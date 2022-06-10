# drone-location-to-lrf.py

When using a DJI drone/payload such as the M30 Series or H20 Series the laser range finder coordinate is written to the metadata. However when opening a photo in a GIS software such as ARCGIS, QGIS, or Google Maps using a tool like photo to pin the photo is displayed at the drone coordinate and there is no option to select the laser range finder location. 

The goal of this script is to allow easy display of drone photos at the coordinates from the laser range finder by replacing the drone lat lon with the laser range finder lat lon.

With the ability of the zoom camera allowing for quick damage assessment, one example would be to place the photos above the house/apartment that a photo is taken of following a natural disaster.

<img src="example.png" width="800">

The script performs this in batch for every valid file within the directory provided and by default does not make copies of the original (can change parameter in main.py). Thus it is reccomended to run this script on copies of the original files if you would like to keep the originals untouched.

1. Install Python (https://www.python.org/downloads/)
2. Install ExifTool (https://exiftool.org/install.html)
3. Download Code

To Run:
Run main.py in terminal/command prompt (python main.py)
OR
Use executable in Dist folder or create your own using Pyinstaller or auto-py-to-exe
