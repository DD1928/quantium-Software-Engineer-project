# import pandas as pd
# import csv
# import os
#
# DATA_DIRECTORY = "./data"
# OUTPUT_FILE_PATH = "./formatted_data.csv"
#
# # open the output file
# with open(OUTPUT_FILE_PATH, "w") as output_file:
# with open(OUTPUT_FILE_PATH, "w", newline="") as output_file: #corrected by me
#     writer = csv.writer(output_file)
#
#     # add a csv header
#     header = ["sales", "date", "region"]
#     writer.writerow(header)
#
#     # iterate through all files in the data directory
#     for file_name in os.listdir(DATA_DIRECTORY):
#         # open the csv file for reading
#         with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
#             reader = csv.reader(input_file)
#             # iterate through each row in the csv file
#             row_index = 0
#             for input_row in reader:
#                 # if this row is not the csv header, process it
#                 if row_index > 0:
#                     # collect data from row
#                     product = input_row[0]
#                     raw_price = input_row[1]
#                     quantity = input_row[2]
#                     transaction_date = input_row[3]
#                     region = input_row[4]
#
#                     # if this is a pink morsel transaction, process it
#                     if product == "pink morsel":
#                         # finish formatting data
#                         price = float(raw_price[1:])
#                         sale = price * int(quantity)
#
#                         # write the row to output file
#                         output_row = [sale, transaction_date, region]
#                         writer.writerow(output_row)
#                 row_index += 1




import os
import pandas as pd

# df=pd.read_csv('data/daily_sales_data_0.csv')
# print(df.head())

# dir_name="data"
# for file in os.listdir(dir_name):
#     print(file)
#     df=pd.read_csv(file)
#     print(df)

import pandas as pd
import os
import glob

# import os
# import pandas as pd
#
# folder_path = './data' # Replace with your actual folder path
# csv_files_list = []
# #writing general csv file search as failsafe
# for filename in os.listdir(folder_path):
#     if filename.endswith('.csv'):
#         file_path = os.path.join(folder_path, filename)
#         csv_files_list.append(file_path)

#code to read header of csv files in folder data
# for file in csv_files_list:
#     df = pd.read_csv(file)
#     header_list = df.columns.tolist()
#     print(header_list)


#combining dataframes for trial
# dataframes = [pd.read_csv(file) for file in csv_files_list] #
# combined_df = pd.concat(dataframes, ignore_index=True) #
# header_list = combined_df.columns.tolist()
# print(header_list)



# final_df.to_csv("pink_morsels.csv", index=False)


# trial 4

#
# import pandas as pd
# import glob
# import os
#
# folder_path = './data' # Replace with your actual folder path
# OUTPUT_FILE_PATH = 'combined_pink_morsel_sales.csv'
# csv_files_list = []
# new_header = ["sales", "date", "region"]
# #writing general csv file search as failsafe
# for filename in os.listdir(folder_path):
#     if filename.endswith('.csv'):
#         file_path = os.path.join(folder_path, filename)
#         csv_files_list.append(file_path)
#
#
#
#
#
# # Define the header for the output file
# new_header = ['Sales', 'Date', 'Region']
#
# # Create an empty list to store filtered dataframes
# filtered_dfs = []
#
# # Loop through all CSV files
# for csv_file in csv_files_list:
#     # Read the data and filter for 'pink morsel' in one go
#     df = pd.read_csv(csv_file)
#     pink_morsel_df = df[df['product'] == 'pink morsel'].copy()  # Use .copy() to avoid SettingWithCopyWarning
#
#     pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '').str.replace(',', '').astype(float)
#     pink_morsel_df['quantity'] = pink_morsel_df['quantity'].astype(int)
#
#     # Calculate the total sales for the filtered data
#     pink_morsel_df['Sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']
#
#     # Select only the relevant columns for the final output
#     # Ensure column names match the new_header
#     final_cols_df = pink_morsel_df[['Sales', 'date', 'region']]
#     final_cols_df.columns = new_header  # Rename columns to match the new header
#
#     # Add the filtered and processed data to the list
#     filtered_dfs.append(final_cols_df)
#
# # Combine all dataframes into a single dataframe
# combined_df = pd.concat(filtered_dfs, ignore_index=True)
#
# # Write the combined dataframe to the output CSV file
# combined_df.to_csv(OUTPUT_FILE_PATH, index=False)  # index=False prevents writing the pandas index

#
# #trial 5 ##SUCCESS
#
#
# import pandas as pd
# import glob
# import os
#
# folder_path = './data' # Replace with your actual folder path
# OUTPUT_FILE_PATH = 'pink_morsel_sales.csv'
# csv_files_list = []
# new_header = ["sales", "date", "region"]
# #writing general csv file search as failsafe
# for filename in os.listdir(folder_path):
#     if filename.endswith('.csv'):
#         file_path = os.path.join(folder_path, filename)
#         csv_files_list.append(file_path)
#
# # combining dataframes for trial
# dataframes = [pd.read_csv(file) for file in csv_files_list] #
# df = pd.concat(dataframes, ignore_index=True) #
#
# # header_list = combined_df.columns.tolist()
# # print(header_list)
#
#
# # Define the header for the output file
# new_header = ['Sales', 'Date', 'Region']
#
# # Create an empty list to store filtered dataframes
# filtered_dfs = []
# #
# pink_morsel_df = df[df['product'] == 'pink morsel'].copy()  # Use .copy() to avoid SettingWithCopyWarning
# pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '').str.replace(',', '').astype(float)
# pink_morsel_df['quantity'] = pink_morsel_df['quantity'].astype(int)
#  # Calculate the total sales for the filtered data
# pink_morsel_df['Sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']
# # Select only the relevant columns for the final output
# # Ensure column names match the new_header
# final_cols_df = pink_morsel_df[['Sales', 'date', 'region']]
# final_cols_df.columns = new_header  # Rename columns to match the new header
#
#
# # Write the combined dataframe to the output CSV file
# final_cols_df.to_csv(OUTPUT_FILE_PATH, index=False)  # index=False prevents writing the pandas index


#trial 6


import pandas as pd
import glob
import os

# folder_path = './data' # Replace with your actual folder path
# OUTPUT_FILE_PATH = 'combined_pink_morsel_sales.csv'
# csv_files_list = []
# new_header = ["sales", "date", "region"]
# #writing general csv file search as failsafe
# for filename in os.listdir(folder_path):
#     if filename.endswith('.csv'):
#         file_path = os.path.join(folder_path, filename)
#         # csv_files_list.append(file_path)


#
# # Define the header for the output file
# new_header = ['Sales', 'Date', 'Region']
#
# # Create an empty list to store filtered dataframes
# filtered_dfs = []
#
# # Loop through all CSV files
# for csv_file in csv_files_list:
#     # Read the data and filter for 'pink morsel' in one go
#     df = pd.read_csv(csv_file)
#     pink_morsel_df = df[df['product'] == 'pink morsel'].copy()  # Use .copy() to avoid SettingWithCopyWarning
#
#     pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '').str.replace(',', '').astype(float)
#     pink_morsel_df['quantity'] = pink_morsel_df['quantity'].astype(int)
#
#     # Calculate the total sales for the filtered data
#     pink_morsel_df['Sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']
#
#     # Select only the relevant columns for the final output
#     # Ensure column names match the new_header
#     final_cols_df = pink_morsel_df[['Sales', 'date', 'region']]
#     # final_cols_df.columns = new_header  # Rename columns to match the new header
#
#     # Add the filtered and processed data to the list
#     filtered_dfs.append(final_cols_df)
#
# # Combine all dataframes into a single dataframe
# combined_df = pd.concat(filtered_dfs, ignore_index=True)
# combined_df.columns = new_header  # Rename columns to match the new header
#
# # Write the combined dataframe to the output CSV file
# combined_df.to_csv(OUTPUT_FILE_PATH, index=False)  # index=False prevents writing the pandas index

#trial 7 #OPTIMISED SUCCESS

#
# import pandas as pd
# import glob
# import os
#
# folder_path = './data'  # Replace with your actual folder path
# OUTPUT_FILE_PATH = 'combined_pink_morsel_sales.csv'
# csv_files_list = []
# new_header = ["sales", "date", "region"]
# filtered_dfs = []
# # writing general csv file search as failsafe
# for filename in os.listdir(folder_path):
#     if filename.endswith('.csv'):
#         file_path = os.path.join(folder_path, filename)
#         # csv_files_list.append(file_path)
#         df = pd.read_csv(file_path)
#         pink_morsel_df = df[df['product'] == 'pink morsel'].copy()  # Use .copy() to avoid SettingWithCopyWarning
#
#         pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '').str.replace(',', '').astype(float)
#         pink_morsel_df['quantity'] = pink_morsel_df['quantity'].astype(int)
#
#             # Calculate the total sales for the filtered data
#         pink_morsel_df['Sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']
#
#             # Select only the relevant columns for the final output
#             # Ensure column names match the new_header
#         final_cols_df = pink_morsel_df[['Sales', 'date', 'region']]
#             # final_cols_df.columns = new_header  # Rename columns to match the new header
#
#             # Add the filtered and processed data to the list
#         filtered_dfs.append(final_cols_df)
#
#         # Combine all dataframes into a single dataframe
# combined_df = pd.concat(filtered_dfs, ignore_index=True)
# combined_df.columns = new_header  # Rename columns to match the new header
#
#         # Write the combined dataframe to the output CSV file
# combined_df.to_csv(OUTPUT_FILE_PATH, index=False)  # index=False prevents writing the pandas index



#
# filtered_dfs = []
#
# # Loop through all CSV files
# for csv_file in csv_files_list:
#     # Read the data and filter for 'pink morsel' in one go
#     df = pd.read_csv(csv_file)
#     pink_morsel_df = df[df['product'] == 'pink morsel'].copy()  # Use .copy() to avoid SettingWithCopyWarning
#
#     pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '').str.replace(',', '').astype(float)
#     pink_morsel_df['quantity'] = pink_morsel_df['quantity'].astype(int)
#
#     # Calculate the total sales for the filtered data
#     pink_morsel_df['Sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']
#
#     # Select only the relevant columns for the final output
#     # Ensure column names match the new_header
#     final_cols_df = pink_morsel_df[['Sales', 'date', 'region']]
#     # final_cols_df.columns = new_header  # Rename columns to match the new header
#
#     # Add the filtered and processed data to the list
#     filtered_dfs.append(final_cols_df)

# # Combine all dataframes into a single dataframe
# combined_df = pd.concat(filtered_dfs, ignore_index=True)
# combined_df.columns = new_header  # Rename columns to match the new header
#
# # Write the combined dataframe to the output CSV file
# combined_df.to_csv(OUTPUT_FILE_PATH, index=False)  # index=False prevents writing the pandas index


