
import pandas as pd
import glob
import os

folder_path = './data' # Replace with your actual folder path
OUTPUT_FILE_PATH = 'pink_morsel_sales.csv'
csv_files_list = []
new_header = ["sales", "date", "region"]
#writing general csv file search as failsafe
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        csv_files_list.append(file_path)

# combining dataframes for trial
dataframes = [pd.read_csv(file) for file in csv_files_list] #
df = pd.concat(dataframes, ignore_index=True) #

# header_list = combined_df.columns.tolist()
# print(header_list)


# Define the header for the output file
new_header = ['Sales', 'Date', 'Region']

#
filtered_df = df[df['product'] == 'pink morsel'].copy()  # Use .copy() to avoid SettingWithCopyWarning
filtered_df['price'] = filtered_df['price'].str.replace('$', '').str.replace(',', '').astype(float)
filtered_df['quantity'] = filtered_df['quantity'].astype(int)
 # Calculate the total sales for the filtered data
filtered_df['Sales'] = filtered_df['price'] * filtered_df['quantity']
# Select only the relevant columns for the final output
# Ensure column names match the new_header
pink_morsels_df = filtered_df[['Sales', 'date', 'region']]
pink_morsels_df.columns = new_header  # Rename columns to match the new header


# Write the combined dataframe to the output CSV file
pink_morsels_df.to_csv(OUTPUT_FILE_PATH, index=False)  # index=False prevents writing the pandas index

####################OR##########################

#
# import pandas as pd
# import glob
# import os
#
# folder_path = './data'  # folder path
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