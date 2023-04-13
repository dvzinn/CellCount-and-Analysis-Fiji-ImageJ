# Cellcount_and_Analysis_Fiji-ImageJ
 Scripts to make counting cells in Fiji ImageJ and saving the data less manual work, written in ImageJ Macro Language and Python.
 This includes:
 1. a script for reverting image colours, stacking those images and saving them (`invert_images.ijm`),
 2. automatically configuring an environment for analysing images, tracking which ones have been analysed already, opening a new image to analyse and saving all changes and the counting data (`set_environment.ijm`),
 3. gathering seperate files as multiple sheets inside one Excel file, filtering the data and calculating contrast for each point (`merge_csv.py`),
 4. and gathering the counted cells per ImageJ Point Tool counter for every brain slice and writing the data into one CSV file (`extract_counts.py`). 

## Installation  
The scripts are available on GitHub https://github.com/dvzinn/Cellcount_and_Analysis_Fiji-ImageJ.git 

Version 1.53t 24 August 2022 of Fiji ImageJ was used during this project.
For viewing and altering code, Visual Studio Code is recommended.

Two libraries have to be installed:
- pandas
- openpyxl
This can be done by writing the following in the terminal: 
```pip install pandas```
```pip install openpyxl```




