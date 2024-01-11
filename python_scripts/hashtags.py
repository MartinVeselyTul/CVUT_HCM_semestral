import extracotrs

"""
This file extracts hashtags from all files in dirpath and works with them.
Preparation for analysis.
"""

"""
Counts hashtags and returns dictionary with hashtags and their counts.
"""
def count_hashtags(data):
    hashtags = {}
    for hashtag in data:
        hashtag = hashtag.lower()
        if hashtag.isascii():
            if hashtag in hashtags:
                hashtags[hashtag] += 1
            else:
                hashtags[hashtag] = 1
    return hashtags

"""
Removes hashtags with count less than 100.
"""
def remove_count_les_100(hashtags):
    hashtags = {key:val for key, val in hashtags.items() if val > 100}
    return hashtags

extracted_hashtags = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_hashtags)
hashtags_counted = remove_count_les_100(count_hashtags(extracted_hashtags))
sorted_hashtags_counted = dict(sorted(hashtags_counted.items(), key=lambda item: item[1], reverse=True))
extracotrs.write_to_file_dict(sorted_hashtags_counted, "./output_data/hashtags_counted.csv")
