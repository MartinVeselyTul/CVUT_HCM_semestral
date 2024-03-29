import json
import gzip
import os
from datetime import datetime

DIRECTORY_PATH = './data/complete_dataset'
TESTING_DIR_PATH = './data/testing_dataset'

"""
Extracts data from all files in directory_path using extraction_function

Args:
    directory_path: path to directory with files (tweets)
    extraction_function: function that extracts data from tweet data (what data are extracted)
    *args: additional arguments for extraction_function

Returns:
    extracted_values: array of extracted values from all files in directory_path
"""
def extract_from_files(directory_path, extraction_function, *args):
    extracted_values = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.gz'):
            file_path = os.path.join(directory_path, filename)
            print("Extracting from file: ", file_path)
            print("Extraction function: ", extraction_function.__name__)
            with gzip.open(file_path, 'rt', encoding='utf-8') as file:
                for line in file:
                    tweet_data = json.loads(line)
                    extracted_data = extraction_function(tweet_data, *args)
                    extracted_values.extend(extracted_data)
    return extracted_values

"""
Returns array of hashtags from tweet data
"""
def extract_hashtags(tweet_data):
    hashtags = tweet_data.get("entities", {}).get("hashtags", [])
    return [hashtag_info.get("text", "") for hashtag_info in hashtags]

"""
Returns user and array of hashtags from tweet data
"""
def extract_hashtags_and_user(tweet_data):
    hashtags = tweet_data.get("entities", {}).get("hashtags", [])
    user = tweet_data.get("user", {}).get("screen_name", [])
    hashtags_arr = [hashtag_info.get("text", "") for hashtag_info in hashtags]
    return [user, hashtags_arr]

"""
Returns array with user and retweeted user from tweet data
"""
def extract_retweets_users(tweet_data):
    retweeted_user = '' #user with original tweet
    who_retweeted = '' #user who retweeted
    tweet_text = tweet_data.get("text", [])
    if str(tweet_text).startswith('RT @'):
        retweeted_user = tweet_text.split('RT @')[1].split(':')[0]
        who_retweeted = tweet_data.get("user", {}).get("screen_name", [])
    return [who_retweeted, retweeted_user]

"""
Returns array with user, number of followers and timestamp from tweet data
"""
def extract_user_followers(tweet_data):
    ids = tweet_data.get("user", {}).get("screen_name", [])
    flws = tweet_data.get("user", {}).get("followers_count", [])
    tim = tweet_data.get("created_at", [])
    tim = int((datetime.strptime(tim, '%a %b %d %H:%M:%S %z %Y')).timestamp())
    data = [ids, flws, tim]
    return data

"""
Returns array with user, number of likes and timestamp from tweet data
"""
def extract_user_favorites(tweet_data):
    ids = tweet_data.get("user", {}).get("screen_name", [])
    flws = tweet_data.get("user", {}).get("favourites_count", [])
    tim = tweet_data.get("created_at", [])
    tim = int((datetime.strptime(tim, '%a %b %d %H:%M:%S %z %Y')).timestamp())
    data = [ids, flws, tim]
    return data

"""
Returns array with user id, user name and number of followers from tweet data
"""
def extract_user_name_id(tweet_data):
    ids = tweet_data.get("user", {}).get("id", [])
    name = tweet_data.get("user", {}).get("screen_name", [])
    followers = tweet_data.get("user", {}).get("followers_count", [])
    return [ids, name, followers]

"""
This function writes data to file.
Args:
    data: data to write to file
    file_path: path to file
Returns:
    Print message that data was written to file
"""
def write_to_file_dict(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for key, value in data.items():
            file.write(str(key) + "," + str(value) + "\n")
    print("Data written to file: ", file_path)

def all_followers_count_user(tweet_data, name):
    flws = 0
    ids = tweet_data.get("user", {}).get("screen_name", [])
    if ids == name:
        flws = tweet_data.get("user", {}).get("followers_count", [])
    return [flws]

"""
Returns timestamp from tweet data (seconds since epoch)
"""
def extract_time(tweet_data):
    tim = tweet_data.get("created_at", [])
    tim = int((datetime.strptime(tim, '%a %b %d %H:%M:%S %z %Y')).timestamp())
    return [tim]

"""
Returns array with 1 if user is in tweet data, 0 otherwise.
Used for counting number of tweets for specific user.
"""
def get_number_of_tweets(tweet_data, user):
    screen_name = tweet_data.get("user", {}).get("screen_name", [])
    if screen_name == user:
        return [1]
    return [0]

"""
Returns array with retweeted user from tweet data.
Used for counting number of retweets.
"""
def get_number_of_retweets(tweet_data):
    retweeted_user = '' #user with original tweet
    tweet_text = tweet_data.get("text", [])
    if str(tweet_text).startswith('RT @'):
        retweeted_user = tweet_text.split('RT @')[1].split(':')[0]
    return [retweeted_user]

"""
Returns array with user name from tweet data.
Used for counting number of tweets.
"""
def get_all_tweets_count(tweet_data):
    screen_name = tweet_data.get("user", {}).get("screen_name", [])
    return [screen_name]

def extract_favorite_tweets(tweet_data):
    user = tweet_data.get("user", {}).get("screen_name", [])
    favorite_count = tweet_data.get("favorite_count", [])
    text = tweet_data.get("text", [])
    return [user, text, favorite_count]

"""
Returns array with first timestamp and last timestamp from tweet data
"""
def get_time_period():
    time_array = extract_from_files(TESTING_DIR_PATH, extract_time)
    time_array.sort()
    return time_array[0], time_array[-1]

if __name__ == "__main__":
    print("Testing...")
