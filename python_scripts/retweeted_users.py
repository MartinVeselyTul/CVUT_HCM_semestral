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

def get_first_item_for_every_key(data):
    export_data = {}
    for key in data.keys():
        for key2 in data[key].keys():
            export_data[key] = key2, data[key][key2]
            print(export_data[key])
            break
    export_data = dict(sorted(export_data.items(), key=lambda item: item[1][1], reverse=True))
    return export_data

def write_to_file_dict(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for key in data.keys():
            file.write(str(key) + "," + str(data[key][0]) +"," + str(data[key][1]) + "\n")
    print("Data written to file: ", file_path)

extracted_retweets = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_retweets_users)
retweets_counted = retweet_count(extracted_retweets)
most_retwitted = who_retweeted_most(retweets_counted)
most_retwitted = get_first_item_for_every_key(most_retwitted)

write_to_file_dict(most_retwitted, "./output_data/retweets_counted_new.csv")