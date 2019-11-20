import json
import os
from collections import OrderedDict


def parse_json(filename):
    new_recipe = OrderedDict()
    with open("./recipes/" + filename, 'r', encoding='utf-8') as json_file:
        recipe = json.load(json_file)
        new_sources = []
        sources = recipe["재료"]
        for title in sources:
            source = sources.get(title)
            for food in source:
                new_source = {}
                new_source["리스트명"] = title
                new_source["식자재명"] = food[0]
                new_source["양"] = food[1]
                new_sources.append(new_source)
        recipe["재료"] = new_sources

    new_recipe["제목"] = recipe["제목"]
    new_recipe["재료"] = recipe["재료"]
    new_recipe["난이도"] = recipe["난이도"]
    new_recipe["태그"] = recipe["태그"]
    new_recipe["양"] = recipe["양"]
    new_recipe["조리방법"] = recipe["조리방법"]
    new_recipe["소요시간"] = recipe["소요시간"]

    with open("./recipes/"+filename, 'w', encoding='utf-8') as make_file:
        json.dump(new_recipe, make_file, ensure_ascii=False, indent='\t')

    return


def main():
    filelist = os.listdir("./recipes")
    for file in filelist[1:]:
        print(file)
        parse_json(file)
    return


if __name__ == '__main__':
    main()