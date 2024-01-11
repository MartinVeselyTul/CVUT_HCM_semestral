import extracotrs

"""
This file returns how many times were specific users tweets retweeted.
It can mean that these users have the biggest influence.
"""
def most_retweeted_users(data):
    export_data = {}
    for i in range(0, len(data), 2):
        retweeted_user = data[i+1]
        if retweeted_user not in export_data.keys():
            export_data[retweeted_user] = 1
        else:
            export_data[retweeted_user] += 1
    return export_data


extracted_retweets = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_retweets_users)

most_retwitted = most_retweeted_users(extracted_retweets)
sorted_most_retwitted = dict(sorted(most_retwitted.items(), key=lambda item: item[1], reverse=True))

extracotrs.write_to_file_dict(sorted_most_retwitted, "./output_data/most_retweeted_users.csv") #nefunguje správně csv