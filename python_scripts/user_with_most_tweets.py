import extracotrs

"""
Udělat výpis top10 uživatelů s nejvíce tweetů.
"""

def count_names(data):
    names = {}
    for name in data:
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    return names

all_tweets = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.get_all_tweets_count)
count_data = count_names(all_tweets)
sorted_data = dict(sorted(count_data.items(), key=lambda item: item[1], reverse=True))

"""
For extraction of top10 users with most tweets
"""
#top10 = dict(list(sorted_data.items())[:10])
#extracotrs.write_to_file_dict(top10, "./output_data/top10_users_tweet_count.csv")

"""
For extraction of number of tweets for each user
"""
#number_of_tweets = dict(list(sorted_data.items()))
#extracotrs.write_to_file_dict(number_of_tweets, "./output_data/users_tweet_count.csv")

names = ["volkansworld", "katayibalqasaa", "ZynabAlAziz", "IsraelsAnalyst", "ImAjayDixit", "ME_Observer_", "indianaftali", "yorumadair", "Spotnewsth", "galida12"]
for name in names:
    if name not in sorted_data:
        sorted_data[name] = 0
    retweets_count = sorted_data[name]
    print(name + " " + str(retweets_count))