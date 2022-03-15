from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import csv

with open("data.csv", "w", encoding="utf8", newline="") as f:
    thewriter= csv.writer(f)
    header = ["Name", "E-mail", "Adresse","Postal Code", "Phone", "Date"]
    thewriter.writerow(header)

path = "/Users/alidemir/Desktop/Önemli/chromedriver"
driver = webdriver.Chrome(path)
def getInfo(page):
    driver.get(f"https://www.avocat-95.fr/recherche-avocat?start={page}")


    main = driver.find_element_by_class_name("jsn-list")
    k = main.text
    k = k.split("\n")

    driver.find_element_by_id("accept_all_g").click()
    sleep(3)
    for p in k:
        driver.find_element_by_link_text(p).click()
        a = driver.find_element_by_class_name("firstnameValue")
        b = driver.find_element_by_class_name("email1Label")
        c = driver.find_element_by_class_name("numero_de_rue_et_voieValue")
        d = driver.find_element_by_class_name("codeValue")
        e = driver.find_element_by_class_name("telephoneValue")
        f = driver.find_element_by_class_name("prestation_de_sermentValue")

        a= a.text
        print(a)
        b = b.text
        c= c.text
        d = d.text
        e = e.text
        f = f.text
        info = [a,b, c,d, e, f]
        thewriter.writerow(info)
        driver.back()
    return

for x in range(0, 400, 100):
    getInfo(x)
    #try:
    #link = WebDriverWait(driver, 10).until(
    #  EC.presence_of_element_located((By.LINK_TEXT, "Claire BENOLIEL"))
    #)
#    link.click()
#   l = WebDriverWait(driver, 10).until(
#      EC.presence_of_element_located((By.CLASS_NAME, "firstnameValue"))
#)
# print(l)
#finally:
#  driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import csv

with open("data.csv", "w", encoding="utf8", newline="") as f:
    thewriter= csv.writer(f)
    header = ["Name", "E-mail", "Adresse","Postal Code", "Phone", "Date"]
    thewriter.writerow(header)

path = "/Users/alidemir/Desktop/Önemli/chromedriver"
driver = webdriver.Chrome(path)
def getInfo(page):
    driver.get(f"https://www.avocat-95.fr/recherche-avocat?start={page}")


    main = driver.find_element_by_class_name("jsn-list")
    k = main.text
    k = k.split("\n")
    print(k)
    l= []

    driver.find_element_by_id("accept_all_g").click()
    sleep(3)
    for p in k:
        driver.find_element_by_link_text(p).click()
        a = driver.find_element_by_class_name("firstnameValue")
        b = driver.find_element_by_class_name("email1Label")
        a = driver.find_element_by_class_name("numero_de_rue_et_voieValue")
        a = driver.find_element_by_class_name("codeValue")
        a = driver.find_element_by_class_name("telephoneValue")
        a = driver.find_element_by_class_name("prestation_de_sermentValue")

    a= a.text
    l.append(a)
    print(l)
    driver.back()


try:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Claire BENOLIEL"))
    )
    link.click()
    l = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "firstnameValue"))
    )
    print(l)
finally:
    driver.quit()

















