import extracotrs
import csv, os

"""
This file extracts users and their used hashtags from all files in dirpath and works with them.
Preparation for analysis.
"""

"""
Counts how many times did user used specific hashtag.
Returns dictionary with users and their hashtags and counts.
"""
def count_hashtags_for_user(data):
    export_data = {}
    for i in range(0, len(data), 2):
        user = data[i]
        hashtags = data[i+1]
        if hashtags != []:
            if user not in export_data:
                export_data[user] = {}
            for hashtag in hashtags:
                hashtag = hashtag.lower()
                if hashtag.isascii():
                    if hashtag in export_data[user]:
                        export_data[user][hashtag] += 1
                    else:
                        export_data[user][hashtag] = 1
    return export_data

"""
Return array with 10 most used hashtags from csv file extracted before.
"""
def get_most_used_hashtags(csv_file):
    hashtags = []
    if not os.path.exists(csv_file):
        print("File does not exist!")
        return
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            hashtags.append(row[0])
    return hashtags[:10]

"""
Returns which users used specific hashtag the most.
"""
def main_distributor(dict_data, hashtag):
    export_data = {}
    for key in dict_data.keys():
        if hashtag in dict_data[key].keys():
            if key not in export_data.keys():
                export_data[key] = dict_data[key][hashtag]
            else:
                export_data[key] += dict_data[key][hashtag]
    return export_data


"""
Dict, ve kterém můžeme dál sledovat, zda v něm jsou podobní uživatelé, kteří by užívali stejné hashtagy.
"""
def dict_aloc(hashtag_dict, new_data, new_key):
    hashtag_dict[new_key] = new_data

extracted_users_hashtags = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_hashtags_and_user)
top_10_hashtags = get_most_used_hashtags('./output_data/hashtags_counted.csv')
users_hashtags_counted = count_hashtags_for_user(extracted_users_hashtags)

hashtags_analyze = {}
for hashtag in top_10_hashtags:
    most_distributed = main_distributor(users_hashtags_counted, hashtag)
    sorted_most_distributed = dict(sorted(most_distributed.items(), key=lambda item: item[1], reverse=True))
    extracotrs.write_to_file_dict(sorted_most_distributed, "./output_data/most_distributed_hashtags/hashtag_distribution_" + hashtag + ".csv")
    dict_aloc(hashtags_analyze, sorted_most_distributed, hashtag)
    print("Hashtag: ", hashtag, " written to file.")
