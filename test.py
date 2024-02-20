import requests
import zipfile
import os
import pandas as pd

def download_and_extract_data(url, output_dir):
    # Download the zip file from the URL
    response = requests.get(url)
    with open("data.zip", "wb") as zip_file:
        zip_file.write(response.content)
    
    # Extract the zip file
    with zipfile.ZipFile("data.zip", 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def get_row_column_count(dataframe):
    # Return the number of rows and columns of DataFrame
    return dataframe.shape[0], dataframe.shape[1]

def select_and_save_columns(dataframe, columns, output_file):
    # Select specific columns and save to a new csv file
    selected_columns = dataframe[columns]
    selected_columns.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Directory to store data
    data_dir = "data"
    
    url_data = "https://drive.google.com/uc?id=1yyL20BNKv3PxJRJVjJ_2Q-HidvIUis45&export=download"

    # Download and extract data
    download_and_extract_data(url_data, data_dir)
    
    # Read csv file
    csv_file_path = os.path.join(data_dir, "customers-100.csv")
    data_df = pd.read_csv(csv_file_path)
    
    # Number of rows and columns
    row_count, column_count = get_row_column_count(data_df)
    print(f"Number of rows: {row_count} \nNumber of columns: {column_count}")
    
    # Select and save specific columns
    selected_columns = ['Index', 'Customer Id', 'First Name', 'Last Name', 'Phone 1']
    select_and_save_columns(data_df, selected_columns, "result.csv")
