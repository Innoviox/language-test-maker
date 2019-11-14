import base
import time

from selenium import webdriver
import os, subprocess, json

from tqdm import tqdm

def read_deck(deck=14):
    cmd = f'curl -X GET "https://karl.qanta.org/api/v1/facts/?deck_id={deck}&user_id=3&limit=10000" -H "accept: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJleHAiOjE1NzQzODk3NDYsInN1YiI6ImFjY2VzcyJ9.qvW6_ji4yj5eHbusgu-2c8AtTK6nB21etiXeJlrL9Eg"'
    a = subprocess.check_output(cmd, shell=True)
    with open("current.txt", "w") as f:
        for i in json.loads(a):
            f.write(i["front"] + "8888" + i["back"] + "\n")

read_deck()

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome('./chromedriver', options=options)
find = driver.find_element_by_xpath

driver.get("https://karl.qanta.org/")
find("/html/body/div/div/div/main/div/div/div/div/div/div[1]/form/div[1]/div[2]/div[1]/div/input").send_keys("sarras305")
find("/html/body/div/div/div/main/div/div/div/div/div/div[1]/form/div[2]/div[2]/div[1]/div/input").send_keys(open("karlpass.txt").read()+"\n")

time.sleep(3)

find("/html/body/div/div/div[3]/div[1]/aside/div[1]/div[3]/div[2]/a/div[2]").click()

time.sleep(3)

find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[3]/div/div/div/div[1]/div[1]/div[1]").click()
time.sleep(1)
deck = 2 # 2 => German, 3 => German Verbs
find(f"/html/body/div/div/div[1]/div/div/div[{deck}]/a/div").click()

def make_cards(word, trans):
    find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[1]/div/div[1]/div/input").send_keys(word)
    find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[2]/div/div[1]/div/input").send_keys(trans)
    find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[3]/button[3]").click()
    time.sleep(1)

    find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[1]/div/div[1]/div/input").send_keys(trans)
    find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[2]/div/div[1]/div/input").send_keys(word)
    find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[3]/button[3]").click()
    time.sleep(1)


lines = [j for i in open("current.txt").readlines() for j in i.split("8888")]

for i in base.word_map.values():
    for word, (trans, _, _) in tqdm(i.items()):
        if word not in lines:
            make_cards(word, trans)
             
##n = 0
##for line in open("quizlet_ex.txt"):
##    try:
##        word, trans = line.split("8888")
##    except KeyboardInterrupt:
##        print(n)
