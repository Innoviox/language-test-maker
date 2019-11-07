import base
import time

base.driver.get("https://karl.qanta.org/")
base.find("/html/body/div/div/div/main/div/div/div/div/div/div[1]/form/div[1]/div[2]/div[1]/div/input").send_keys("sarras305")
base.find("/html/body/div/div/div/main/div/div/div/div/div/div[1]/form/div[2]/div[2]/div[1]/div/input").send_keys(open("karlpass.txt").read()+"\n")

time.sleep(3)

base.find("/html/body/div/div/div[3]/div[1]/aside/div[1]/div[3]/div[2]/a/div[2]").click()

time.sleep(3)

base.find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[3]/div/div/div/div[1]/div[1]/div[1]").click()
time.sleep(1)
base.find("/html/body/div/div/div[1]/div/div/div[2]/a/div/div").click()

for i in base.word_map.values():
    for word, (trans, _, _) in i.items():
        base.find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[1]/div/div[1]/div/input").send_keys(word)
        base.find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[2]/form/div[2]/div/div[1]/div/input").send_keys(trans)
        base.find("/html/body/div/div/div[3]/div[1]/main/div/div/div/div[3]/button[3]").click()

        time.sleep(1)        
