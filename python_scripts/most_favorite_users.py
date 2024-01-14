import extracotrs
import followers_increase as fol

data = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.extract_user_favorites)
data_beginning = fol.first_followers_count(data)
data_end = fol.last_followers_count(data)
data_compared = fol.compare_followers(data_beginning, data_end)

extracotrs.write_to_file_dict(data_compared, "output_data/most_liked_users.csv")
