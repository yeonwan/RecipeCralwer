from urllib.error import HTTPError
from selenium import webdriver
from collections import OrderedDict
import selenium.common.exceptions as Error
import urllib.request
import numpy as np
import time
import json
import os


def parse_ingre(li):
    category_idx = []
    ingre_dic = {}
    for idx, val in enumerate(li):
        if val[0] == '[':
            category_idx.append((idx, val))

    length = len(category_idx)
    for i in range(length):
        idx, val = category_idx[i]
        if i == length-1:
            val = val[1:-1]
            sub = li[idx + 1:]
        else:
            nidx, _ = category_idx[i + 1]
            val = val[1: -1]
            sub = li[idx + 1: nidx]

        nrow = len(sub) / 2
        sub = np.array(sub)
        sub = sub.reshape(int(nrow), 2)
        sub = np.ndarray.tolist(sub)
        ingre_dic[val] = sub
    return ingre_dic


def crawl_recipe(driver, recipe_num):
    recipe_step = []
    try:
        url_full = "http://www.10000recipe.com/recipe/" + recipe_num
        driver.get(url_full)

        recipe_title = driver.find_element_by_tag_name("h3").text
        recipe_source = driver.find_element_by_class_name("ready_ingre3").text.split('\n')
        recipe_sources = parse_ingre(recipe_source)
        consumed_time = driver.find_element_by_class_name("view2_summary_info2").text
        proportion_of_food = driver.find_element_by_class_name("view2_summary_info1").text
        difficulty = driver.find_element_by_class_name("view2_summary_info3").text
        recipe_tags = driver.find_element_by_class_name("view_tag").text.split("#")
        recipe_tags.remove('')
        num = 1
        while True:
            try:
                recipe_step.append(driver.find_element_by_id("stepdescr" + str(num)).text)
                num += 1
            except Error.NoSuchElementException as e:
                break
        img = driver.find_element_by_class_name('centeredcrop').find_element_by_id("main_thumbs").get_attribute("src")
        urllib.request.urlretrieve(img, "./images/"+recipe_num +".png")
        recipe = OrderedDict()
        recipe["제목"] = recipe_title
        recipe["재료"] = recipe_sources
        recipe["조리방법"] = recipe_step
        recipe["소요시간"] = consumed_time
        recipe["난이도"] = difficulty
        recipe["양"] = proportion_of_food
        recipe["태그"] = recipe_tags
        with open('recipes/' + recipe_num+".json", 'w', encoding='utf-8') as mk_file:
            json.dump(recipe, mk_file, 'w', ensure_ascii=False, indent='\t')

    except HTTPError as e:
        #print(e.msg)
        return False
    except ValueError as e1:
        #print(e1)
        return False
    except TypeError as e2:
        #print(e2)
        return False
    except Error.NoSuchElementException:
        #print(e3.msg)
        return False
    except Error.UnexpectedAlertPresentException:
        #print(e3.msg)
        return False

    return True


def main():
    driver = webdriver.Chrome("C:/Users/yeonwan/Desktop/2019-2/AIStartUp/Study/crawl/chromedriver")
    total_num = 0
    flist = os.listdir('./recipes')
    fdic = dict.fromkeys(flist,1)
    rnum = 6920000
    while rnum < 7000000 and total_num < 5000:
        if fdic.get(str(rnum)+'.json') == 1:
            total_num += 1
            rnum += 1
            continue
        if crawl_recipe(driver, str(rnum)): total_num += 1
        rnum += 1
        if total_num % 10 == 1:
            print("{} recipe crawled, {}% completed.".format(total_num, total_num/50))
    driver.quit()


if __name__ == '__main__':
    main()


