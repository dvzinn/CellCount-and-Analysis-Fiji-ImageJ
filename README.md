# Cellcount-and-Analysis-Fiji-ImageJ
 Scripts to make counting cells in Fiji ImageJ and saving the data less manual work, written in ImageJ Macro Language and Python.
 This includes:
 1. `invert_images.ijm`: reverting image colours, stacking those images and saving them,
 2. `set_environment.ijm`: automatically configuring an environment for analysing images, tracking which ones have been analysed already, opening a new image to analyse and saving all changes and the counting data,
 3. `merge_csv.py`: gathering seperate files as multiple sheets inside one Excel file, filtering the data and calculating contrast for each point,
 4. `extract_counts.py`: and gathering the counted cells per ImageJ Point Tool counter for every brain slice and writing the data into one CSV file. 

`set_environment.ijm` is likely the most generally useful script, the other scripts are not necesserily needed to make use of this.

## Installation  
The scripts are available on GitHub: https://github.com/dvzinn/CellCount-and-Analysis-Fiji-ImageJ.git.

Version 1.53t 24 August 2022 of Fiji ImageJ was used during this project.
For viewing and altering code, Visual Studio Code is recommended.

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
Every code file has a protocol which are also available on GitHub: https://github.com/dvzinn/CellCount-and-Analysis-Fiji-ImageJ.git.
- `ImageJ invert_images.ijm` for `invert_images.ijm`.
- `ImageJ set_environment protocol.pdf` for `set_environment.ijm`.
- `Python merge_csv protocol.pdf` for `merge_csv.py`.
- `Python extract_counts.pdf` for `extract_counts.py`.

For optimal use, the protocols and code should be used in this order (if all needed).

## Limitations
- After making changes in the ImageJ code files, ImageJ should be restarted. 
- Running `merge_csv.py` and `extract_counts.py` multiple times without changing the file, will overwrite the files.
