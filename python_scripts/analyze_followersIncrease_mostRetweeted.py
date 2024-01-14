import csv
from itertools import islice


def load_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def find_same_users(file1, file2):
    users = {}
    for i in range(0, len(file1)):
        for j in range(0, len(file2)):
            if int(file1[i][1]) > 100 and int(file2[j][1]) > 100:
                if file1[i][0] == file2[j][0]:
                    new_user = (file1[i][1], file2[j][1])
                    users[file1[i][0]] = new_user
                if len(users) == 20:
                    return users
    return users

def save_to_csv(data, file_path):
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        for key, value in data.items():
            writer.writerow([key, value[0], value[1]])


followers_increase = load_csv_file("./output_data/followers_count_increase_name.csv")
most_retweeted_users = load_csv_file("./output_data/most_retweeted_users.csv")

same_users = find_same_users(followers_increase, most_retweeted_users)

save_to_csv(same_users, "./output_data/analyze_followers_retweets.csv")


