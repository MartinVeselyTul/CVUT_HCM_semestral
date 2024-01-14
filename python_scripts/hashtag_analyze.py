import csv
import extracotrs

"""
For the most used hashtags and who used them the most this file will write how much of these hashtags speicific users used.
"""

def load_csv2(file_path):
    data_output = list()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            arr = row[0].split(";")
            for i in range(0, len(arr)):
                if arr[i] != "":
                    data_output.append(arr[i])
    return data_output

def work(arr):
    output = {}
    for word in arr:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    return output

"""
data = load_csv2("./excel_data/top5_hashtags.csv")
data = work(data)
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(sorted_data)
"""

def count_1(data):
    count = 0
    for i in range(0, len(data)):
        if data[i] == 1:
            count += 1
    return count

name_count = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.get_number_of_tweets, ("VishnuTiwa29296"))
print(count_1(name_count))