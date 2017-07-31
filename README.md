# georeferencer
Script for georeferencing aerial images with GDAL given magnetometer and IMU readings

### Workflow

1. R calculates corner coordiantes using package `geosphere`
2. Python writes CSV to batch file
3. Batchfile runs GDAL_translate.exe on images