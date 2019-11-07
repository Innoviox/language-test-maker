import base

base.driver.get("https://karl.qanta.org/")
base.find("/html/body/div/div/div/main/div/div/div/div/div/div[1]/form/div[1]/div[2]/div[1]/div/input").send_keys("sarras305")
base.find("/html/body/div/div/div/main/div/div/div/div/div/div[1]/form/div[2]/div[2]/div[1]/div/input").send_keys(open("karlpass.txt").read()+"\n")

base.driver.get("https://karl.qanta.org/main/add/fact")

print(word_map.keys())
import pdb; pdb.set_trace()
