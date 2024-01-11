import extracotrs

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
    return export_data


extracted_followers = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_user_followers)

followers_count_start = first_followers_count(extracted_followers)
followers_count_end = last_followers_count(extracted_followers)
followers_count_increase = compare_followers(followers_count_start, followers_count_end)
sorted_followers_count_increase = dict(sorted(followers_count_increase.items(), key=lambda item: item[1], reverse=True))

extracotrs.write_to_file_dict(sorted_followers_count_increase, "./output_data/followers_count_increase.csv")