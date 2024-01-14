import extracotrs


count = extracotrs.extract_from_files(extracotrs.TESTING_DIR_PATH, extracotrs.all_followers_count_user, "volkansworld")

for i in count:
    if i == 0:
        count.remove(i)

print(count)