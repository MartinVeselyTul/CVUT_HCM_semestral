import extracotrs

"""
This file saves user name and user id to file for further analysis.
"""

"""
Returns dictionary with user id and user name from tweet data for users that has more than 100 followers.
"""
def data_to_dict(data):
    export_data = {}
    for i in range(0, len(data), 3):
        id = data[i]
        user = data[i+1]
        followers = data[i+2]
        if int(followers) > 100:
            if id not in export_data.keys():
                export_data[id] = user
    return export_data

extracted_data = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_user_name_id)
data_dict = data_to_dict(extracted_data)
extracotrs.write_to_file_dict(data_dict, "./output_data/user_name_and_id.csv")