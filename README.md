# Cellcount-and-Analysis-Fiji-ImageJ
 Scripts to make counting cells (e.g. after immunohistochemistry) in Fiji ImageJ and saving the data less manual work, written in ImageJ Macro Language and Python.
 This includes:
 1. `invert_images.ijm`: inverting image colours, stacking those images and saving them,
 2. `set_environment.ijm`: automatically configuring an environment for analysing images, tracking which ones have been analysed already, opening a new image to analyse and saving all image changes and the counting + ROI (Region of Interest) data,
 3. `merge_csv.py`: gathering seperate files as multiple sheets inside one Excel file, filtering the data and calculating contrast for each point,
 4. `extract_counts.py`: gathering the counted cells per ImageJ Point Tool counter for every brain slice and writing the data into one CSV file,
 5. `merge_counts_ROI.py`: and combining the counted cells with the measured ROI data into one CSV file.

`set_environment.ijm` is likely the most generally useful script, the other scripts are not necesserily needed to make use of this.

## Installation  
The scripts are available on GitHub: https://github.com/dvzinn/CellCount-and-Analysis-Fiji-ImageJ.git.

Version 1.53t 24 August 2022 of Fiji ImageJ was used during this project.
For viewing and altering Python code (".py"), Visual Studio Code is recommended. For altering the ".ijm" code files, Fiji ImageJ is recommended.

Two libraries have to be installed for the Python scripts:
- pandas
- openpyxl

This can be done by writing the following in the terminal: 
```bash
pip install pandas
```
```bash
pip install openpyxl
```

## Configuration and Implementation
All code files have a protocols, which are also available on GitHub: https://github.com/dvzinn/CellCount-and-Analysis-Fiji-ImageJ.git.
- `ImageJ invert_images.ijm` for `invert_images.ijm`.
- `ImageJ set_environment protocol.pdf` for `set_environment.ijm`.
- `Python merge_csv protocol.pdf` for `merge_csv.py`.
- `Python extract_counts.pdf` for `extract_counts.py`.
- The protocol for `merge_counts_ROI.py` is still in progress.

For optimal use, the protocols and code should be used in this order (if all are needed).

## Limitations
- After making changes in the ImageJ code files, ImageJ should be restarted. 
- Running `merge_csv.py`, `extract_counts.py` or `merge_counts_ROI.py` multiple times without changing the file, will overwrite the files.
