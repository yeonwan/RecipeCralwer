import requests
import json
import os
from collections import OrderedDict


def store(filename, _id):

    URL = "http://ec2-15-164-218-30.ap-northeast-2.compute.amazonaws.com:9200/test/recipe/"+str(_id)

    with open("./recipes/" + filename, 'r', encoding='utf-8') as f:
        new_recipe = OrderedDict()
        recipe = json.load(f)
        new_recipe["제목"] = recipe["제목"]
        new_recipe["재료"] = recipe["재료"]
        new_recipe["난이도"] = recipe["난이도"]
        new_recipe["태그"] = recipe["태그"]
        new_recipe["양"] = recipe["양"]
        new_recipe["조리방법"] = recipe["조리방법"]
        new_recipe["소요시간"] = recipe["소요시간"]
        headers = {"Content-Type" : "application/json"}
        res = requests.put(URL, data=json.dumps(new_recipe), headers=headers)

    return


def main():
    flist = os.listdir("./recipes")
    _id = 1
    for f in flist:
        store(f, _id)
        _id += 1
        if _id % 100 == 0:
            print("task " + str(_id / 15) + "% completed")
    return


if __name__ == '__main__':
    main()