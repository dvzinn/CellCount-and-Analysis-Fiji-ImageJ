# EXTRACT COUNTS
# Daniëlla Zinn <daniellazinn@hotmail.nl>
# April 2023

# import libraries
import pandas as pd

# since the backward slash "\" is a special charactor in Python strings, an "r" should be placed before the string (to indicate a raw string literal)
# for non-Windows users: the "r" can be removed if the path includes forward slashes
path = r"C:\Users\Danie\Documents\Internship\Counting\Merge_data.xlsx" # specify path to Excel file with data from all slices in multiple sheets
counting_results = r"C:\Users\Danie\Documents\Internship\Counting\Counting_results.csv" # specifiy path to an existing empty CSV for saving the data

dataframes = pd.read_excel(path, sheet_name=None) # read the Excel file into a dictionary of dataframes

result = [] #initialize an empty list result to store the results of data processing

# for every dataframe in the dataframes dictionary:
for (filename, data) in dataframes.items():
    # initialize two variables counted_upper and counted_lower to 0, which will be used to store the calculated counts
    counted_upper = 0
    counted_lower = 0

    # if value 1 exists in the "Counter" column of the dataframe, calculate the mean of the "Count" column for rows where the "Counter" column is equal to 
    # 1 and save the calculated mean in the counted_upper variable
    if 1 in data["Counter"].values:
        counted_upper = round(data[data["Counter"] == 1]["Count"].mean())

    # if value 2 exists in the "Counter" column of the dataframe, calculate the mean of the "Count" column for rows where the "Counter" column is equal to 
    # 2 and save the calculated mean in the counted_lower variable   
    if 2 in data["Counter"].values:
        counted_lower = round(data[data["Counter"] == 2]["Count"].mean())
    
    # append a list [filename, counted_upper, counted_lower] to the result list, where filename is the key of the current dataframe in the dataframes 
    # dictionary, and counted_upper and counted_lower are the calculated counts for "Counter" values 1 and 2 respectively
    result.append([filename, counted_upper, counted_lower])

# convert the result list into a DataFrame called "table" with column names "Filename", "Counted upper", and "Counted lower"
table = pd.DataFrame(result, columns = ["Filename", "Counted upper", "Counted lower"])

table.to_csv(counting_results) # write the table DataFrame to a CSV file specified in the "counting_results" variable

