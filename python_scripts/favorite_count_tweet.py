import extracotrs

"""
This file is checking most favorited tweets. - error, every tweet has 0 like
"""

def count_and_sort_tweets(data):
    return_data = {}
    for i in range(0, len(data),3):
            return_data[data[i]] = data[i+2]
    return_data = dict(sorted(return_data.items(), key=lambda item: item[1], reverse=True))
    top50 = dict(list(return_data.items())[:50])
    return top50
        

favorite_tweets = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_favorite_tweets)
sorted_data = count_and_sort_tweets(favorite_tweets)
extracotrs.write_to_file_dict(sorted_data, "./output_data/top50_favorite_tweets.csv")