# import base
import time

from selenium        import webdriver

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
find("/html/body/div/div/div[1]/div/div/div[3]/a/div").click()

# for i in base.word_map.values():
#     for word, (trans, _, _) in i.items():
n = 0
for line in open("quizlet_ex.txt"):
    try:
        word, trans = line.split("8888")
        find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[1]/div/div[1]/div/input").send_keys(word)
        find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[2]/div/div[1]/div/input").send_keys(trans)
        find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[3]/button[3]").click()
        n += 1
        time.sleep(1)

        find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[1]/div/div[1]/div/input").send_keys(trans)
        find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[2]/div/div[1]/div/input").send_keys(word)
        find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[3]/button[3]").click()
        n += 1
        time.sleep(1)
    except KeyboardInterrupt:
        print(n)
