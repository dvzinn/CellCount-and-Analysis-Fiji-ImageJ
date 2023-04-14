# MERGE CSV
# Daniëlla Zinn <daniellazinn@hotmail.nl>
# April 2023

# WARNING, this script will overwrite an existing file if the document in "merge_data" is not changed

# import libraries
import pandas as pd
import glob
import openpyxl # this may not import well in the script; if so, run this script in the terminal

# Folder in which the CSV files with counting data are stored. Since the backward slash "\" is a special character in Python strings, an "r" should be placed
# before the string. If the path includes forward slashes, the "r" can be removed. Important to add an asterisk "*" at the end of the path.
measurements = r"C:\Users\Danie\Documents\Internship\Counting\Measurements\*"
# empty Excel file that will be used to write all data to:
merge_data = r"C:\Users\Danie\Documents\Internship\Counting\Merge_data.xlsx"

dataframes = {} # initialise an empty dictionary called dataframes that will be used to store the processed data 

# iterates over all the files in the directory
# the glob.glob() function is used to find all the files in the directory that match the specified pattern, which in this case is "*" (i.e., all files) for
# every file in measurements:
for f in glob.glob(measurements):
    data = pd.read_csv(f)

    # Use lines 23 - 44 if certain counters are used for measuring contrast. In this case, counter 1 and 2 contain the real data, counters 3 (beloning to 1)
    # and 4 (beloning to 2) include measurements of points that were placed next to the measurements, to calculate contrast. This code subtracts the value
    # of the 1st counter from the 3rd counter, and the 2nd counter from the 4th counter. This code can be commented if not needed.
    
    # initialise an empty pandas Series called contrast_one, which will be used to calculate and store the contrast value for counter 1.
    contrast_one = pd.Series([], dtype=float)
    # initialise an empty pandas Series called contrast_two, which will be used to calculate and store the contrast value for counter 2.
    contrast_two = pd.Series([], dtype=float)

    # if counter 1 and 3 values are present, subtract counter 1 values from the mean of the counter 3 values
    if 1 in data["Counter"].values and 3 in data["Counter"].values:
        mean_three = round(data[data["Counter"] == 3]["Mean"].mean())
        contrast_one = mean_three - data[data["Counter"] == 1]["Mean"]     

    # if counter 2 and 4 values are present, subtract counter 2 values from the mean of the counter 4 values
    if 2 in data["Counter"].values and 4 in data["Counter"].values:
        mean_four = round(data[data["Counter"] == 4]["Mean"].mean())
        contrast_two = mean_four - data[data["Counter"] == 2]["Mean"]

    # add a column named "Contrast", consisting of the values in contrast_one and contrast_two
    data["Contrast"] = pd.concat([contrast_one, contrast_two])
    data = data[data["Counter"] <= 2]  # filter the data by selecting only the rows where the values in the "Counter" column are less than or equal to 2
    # if you want to include more counters, the 2 can be changed in the amount of counters of interest
    # the filtered DataFrame is then assigned back to the data variable, effectively removing rows where the "Counter" value is greater than 2 from the DataFrame


    # delete the columns that are not needed
    del data["Area"]
    del data["Min"]
    del data["Max"]
    del data["Slice"]

    dataframes[f.split("\\")[-1][:-4]] = data # split the filepath into smaller pieces on the places with backwardslashes, select the last part and save all 
    # characters in the string from the beginning up to (but not including) the last 4 characters in "dataframes", which in this case would exclude ".csv"

# write multiple dataframes to an Excel file (in the earlier specified "merge_data" file)
with pd.ExcelWriter(merge_data) as writer: 
    for (filename, data) in dataframes.items():
        data.to_excel(writer, sheet_name=filename) # output will be one Excel file with multiple sheets which will be named after the original files
