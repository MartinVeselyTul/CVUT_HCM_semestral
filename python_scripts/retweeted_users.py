import extracotrs

"""
Counts retweets of each user
return: {user: {retweeted_user, count}}
"""
def retweet_count(data):
    export_data = {} 
    for i in range(0, len(data), 2):
        if data[i] == '':
            continue
        if data[i] not in export_data.keys():
            export_data[data[i]] = {}
            export_data[data[i]][data[i+1]] = 1
        else:
            if data[i+1] in export_data[data[i]].keys():
                export_data[data[i]][data[i+1]] += 1
            else:
                export_data[data[i]][data[i+1]] = 1
        export_data[data[i]] = dict(sorted(export_data[data[i]].items(), key=lambda item: item[1], reverse=True))        
    return export_data
            
"""
Sorts users by number of retweets
"""
def who_retweeted_most(dict_data):
    dict_data = dict(sorted(dict_data.items(), key=lambda x: sum(x[1].values()), reverse=True))
    return dict_data


extracted_retweets = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_retweets_users)
retweets_counted = retweet_count(extracted_retweets)
most_retwitted = who_retweeted_most(retweets_counted)

extracotrs.write_to_file_dict(most_retwitted, "./output_data/retweets_counted.txt")