# georeferencer
Script for georeferencing aerial images with GDAL given magnetometer and IMU readings

### Workflow

1. Payload captures images and notes bearing (magnetometer), pitch, roll, and yaw (IMU)
2. R calculates corner coordinates using package `geosphere` given camera FOV and writes to CSV file
3. Python writes CSV file to batch file of GDAL commands
4. Batchfile runs GDAL_translate.exe on images using corner coordinates as Ground Control Points (GCP)
