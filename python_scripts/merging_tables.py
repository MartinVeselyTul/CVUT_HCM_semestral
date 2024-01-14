import csv
import pandas as pd
"""
how the increase in the number of followers based on the retweet of a given user is reflected
"""

def load_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def merge_csv(file1, file2):
    # Convert the loaded data to DataFrames without specifying column names
    df1 = pd.DataFrame(file1)
    df2 = pd.DataFrame(file2)

    print(df2)

    # Merge the tables based on the first column (index 0)
    merged_table = pd.merge(df1, df2, left_on=0, right_on=0)
    merged_table = merged_table.drop(columns=[0])
    print(merged_table['1_y'].max())
    merged_table = merged_table.sort_values(by=merged_table.columns[1], ascending=False)
    return merged_table

    
most_retweeted_users = load_csv_file("./output_data/most_retweeted_users.csv")
followers_increase = load_csv_file("./output_data/followers_count_increase.csv")

table_most_increase = pd.read_csv("./output_data/followers_count_increase.csv")
table_user_id = pd.read_csv("./output_data/user_name_and_id.csv")

user_id = load_csv_file("./output_data/user_name_and_id.csv")

data = merge_csv(user_id, followers_increase)

#data.to_csv("./output_data/analyze_followers_count_increase.csv", index=False)