
dict_test = {}
dict_test["kdo1"] = {"koho1": 1, "koho2": 2}
dict_test["kdo2"] = {"koho1": 1, "koho2": 2}

dict3 = {}
for key in dict_test.keys():
    for key2 in dict_test[key].keys():
        dict3[key] = key2, dict_test[key][key2]
        break

print(dict3["kdo1"][1])