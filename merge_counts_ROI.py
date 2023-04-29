# EXTRACT COUNTS
# Daniëlla Zinn <daniellazinn@hotmail.nl>
# April 2023

# import libraries
import pandas as pd
import glob
import csv

# since the backward slash "\" is a special charactor in Python strings, an "r" should be placed before the string (to indicate a raw string literal)
# for non-Windows users: the "r" can be removed if the path includes forward slashes
ROI_folder = r"C:\Users\Danie\Documents\Internship\Counting\ROI_folder\*" # folder with the ROI measurements
counting_results = r"C:\Users\Danie\Documents\Internship\Counting\Counting_results.csv" # folder in which the already existing file exists that you want to add new data to
new_data = r"C:\Users\Danie\Documents\Internship\Counting\New_data.csv" # file with new data added to the old data

dataframes = {} # initialise an empty dictionary called dataframes that will be used to store the processed data 

# open the counting_results file in read mode and create a reader object
with open(counting_results,"r") as csvinput:
    reader_obj = csv.reader(csvinput)

    # create a new_data file in write mode and create a writer object
    with open(new_data, "w") as csvoutput:
        writer_obj = csv.writer(csvoutput, lineterminator='\n')
        
        # copy the data from the counting_results file to the new_data file
        for copy_data in reader_obj:
            writer_obj.writerow(copy_data)

# read the data from the new_data file into a pandas DataFrame
new_data_df = pd.read_csv(new_data)

# add two new columns for 'Upper Blade Area' and 'Lower Blade Area' to the new_data_df DataFrame
new_data_df['Upper Blade Area'] = None
new_data_df['Lower Blade Area'] = None

# loop through all files in the ROI_folder directory using glob
for f in glob.glob(ROI_folder):
    # read the data from the current file into a pandas DataFrame
    data = pd.read_csv(f)
    
    # initialise an empty pandas Series called upper_area, which will be used to store the "Upper Blade Area" data
    upper_area = pd.Series([], dtype=float)
    # initialise an empty pandas Series called contrast_two, which will be used to calculate and store the value for Lower Blade Area
    lower_area = pd.Series([], dtype=float)
    
    upper_area = data.loc[0,"Area"] #locate the first datapoint in the column named "Area" and store it in the "upper_area" variable
    lower_area = data.loc[1 ,"Area"] #locate the second datapoint in the column named "Area" and store it in the "lower_area" variable

    # add the 'Upper Blade Area' and 'Lower Blade Area' columns to the data DataFrame and fill them with the respective data
    data['Upper Blade Area'] = upper_area 
    data['Lower Blade Area'] = lower_area

    # extract the filename from the file path and save it in the dataframes dictionary as the key
    filename = f.split("\\")[-1][:-8]
    dataframes[filename] = data # split the filepath into smaller pieces on the places with backwardslashes, select the last part and save all 
    # characters in the string from the beginning up to (but not including) the last 4 characters in "dataframes", which in this case would exclude "_ROI.csv"

for filename, data in dataframes.items():
    # locate the corresponding row in the df dataframe based on the filename and update the row with the new data
    row_index = new_data_df.index[new_data_df['Filename'] == filename].tolist()[0]
    new_data_df.at[row_index, 'Upper Blade Area'] = dataframes[filename].loc[0, 'Area']
    new_data_df.at[row_index, 'Lower Blade Area'] = dataframes[filename].loc[1, 'Area']

# write the updated dataframe back to the new_data CSV file
new_data_df.to_csv(new_data, index=False)
