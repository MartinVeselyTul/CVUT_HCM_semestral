import extracotrs
import os

"""
This file is checking which users have the most followers incease. 
"""

"""
This function returns number of followers for user at the end of the period.
"""
def last_followers_count(data):
    export_data = {}
    for i in range(0, len(data), 3):
        if data[i] not in export_data.keys():
            export_data[data[i]] = data[i+1], data[i+2] #id: {followers, timestamp}
        else:
            if export_data[data[i]][1] < data[i+2]:
                export_data[data[i]] = data[i+1], data[i+2]
    return export_data

"""
This function returns number of followers for user at the beginning of the period.
"""
def first_followers_count(data):
    export_data = {}
    for i in range(0, len(data), 3):
        if data[i] not in export_data.keys():
            export_data[data[i]] = data[i+1], data[i+2] #id: {followers, timestamp}
        else:
            if export_data[data[i]][1] > data[i+2]:
                export_data[data[i]] = data[i+1], data[i+2]
    return export_data

"""
This function copmares the difference between followers at the beginning and at the end of the period.
"""
def compare_followers(start, end):
    export_data = {}
    for key in start.keys():
        if key in end.keys():
            if int(start[key][0]) < int(end[key][0]):
                export_data[key] = int(end[key][0]) - int(start[key][0])
    export_data = dict(sorted(export_data.items(), key=lambda item: item[1], reverse=True))
    return export_data

"""
Returns only first followers count for users that have more than 1000 followers.
"""
def only_first_followers_count(data):
    export_data = {}
    for key in data.keys():
        if int(data[key][0]) > 1000:
            export_data[key] = int(data[key][0])
    sorted_data = dict(sorted(export_data.items(), key=lambda item: item[1], reverse=True))
    return sorted_data

"""
Returns the difference between followers at the beginning and at the end of the period.
"""
def compare_followers_full_data(start, end):
    export_data = {}
    for key in start.keys():
        if key in end.keys():
            if (int(start[key][0]) < int(end[key][0])) and (int(start[key][0]) > 1000):
                increase = int(end[key][0]) - int(start[key][0])
                export_data[key] = increase, int(start[key][0]), int(end[key][0]), float((increase/(int(start[key][0])/100)))
    #sort array by 4th value in tuple
    export_data = dict(sorted(export_data.items(), key=lambda item: item[1][3], reverse=True))
    return export_data
    
def save_tuple_csv(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for key, value in data.items():
            file.write(str(key) + "," + str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n")
    print("Data written to file: ", file_path)

extracted_followers = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_user_followers)

followers_count_start = first_followers_count(extracted_followers)
#first = only_first_followers_count(followers_count_start)
#sorted_followers_start = dict(sorted(followers_count_start.items(), key=lambda item: item[1], reverse=True))
followers_count_end = last_followers_count(extracted_followers)
#followers_count_increase = compare_followers(followers_count_start, followers_count_end)
#sorted_followers_count_increase = dict(sorted(followers_count_increase.items(), key=lambda item: item[1], reverse=True))

#extracotrs.write_to_file_dict(sorted_followers_count_increase, "./output_data/followers_count_increase_name.csv")

data_full = compare_followers_full_data(followers_count_start, followers_count_end)

save_tuple_csv(data_full, "./output_data/users_followers_full_info_by_percentage.csv")