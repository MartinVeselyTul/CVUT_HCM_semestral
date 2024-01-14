import extracotrs
import followers_increase as fol
import user_with_most_tweets as umt

def count_average_like_per_tweet(likes, number_of_tweets):
    export_data = {}
    for key in likes.keys():
        if key in number_of_tweets.keys():
            export_data[key] = likes[key] / number_of_tweets[key]
    export_data = dict(sorted(export_data.items(), key=lambda item: item[1], reverse=True))
    top50 = dict(list(export_data.items())[:50])
    return top50

data = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_user_favorites)
data_beginning = fol.first_followers_count(data)
data_end = fol.last_followers_count(data)
data_compared = fol.compare_followers(data_beginning, data_end)

all_tweets = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.get_all_tweets_count)
count_data = umt.count_names(all_tweets)
sorted_data = dict(sorted(count_data.items(), key=lambda item: item[1], reverse=True))
number_of_tweets = dict(list(sorted_data.items()))

data_average = count_average_like_per_tweet(data_compared, number_of_tweets)
extracotrs.write_to_file_dict(data_average, "output_data/average_like_per_tweet.csv")