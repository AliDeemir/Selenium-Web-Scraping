#Import necessary packages

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import csv

#Create a csv files with headers
with open("data.csv", "w", encoding="utf8", newline="") as f:
    thewriter= csv.writer(f)
    header = ["Name", "E-mail", "Adress","Postal Code", "Phone", "Date"]
    thewriter.writerow(header)

#Define chrome webdriver path
path = "/Users/alidemir/Desktop/Önemli/chromedriver"
driver = webdriver.Chrome(path)

#Open the source page
driver.get("https://www.avocat-95.fr/recherche-avocat?start=0")

#Accept the cookies
driver.find_element_by_id("accept_all_g").click()

#Define the function for scraping
def getInfo(page):

    #Open the page with defined page number
    driver.get(f"https://www.avocat-95.fr/recherche-avocat?start={page}")

    #Collect the names of members and create list
    main = driver.find_element_by_class_name("jsn-list")
    k = main.text
    k = k.split("\n")

    #Open csv file and get ready to append collected info
    with open("data.csv", "a", encoding="utf8", newline="") as f:

        thewriter= csv.writer(f)

        #Go into collected list of names one by one
        for p in k:
            #Then click the names
            driver.find_element_by_link_text(p).click()
            #Try collecting information and if it fails to collect skip and write that there is no info about that person
            try:
                name = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "firstnameValue"))
                ).text
            except: name="No Name"
            try:
                email = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "email1Value"))
                ).text
            except: email="No e-mail"
            try:
                adress = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "numero_de_rue_et_voieValue"))
                ).text
            except: adress="No adress"
            try:
                postCode = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "codeValue"))
                ).text
            except: postCode="No postal code"
            try:
                telephone = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "telephoneValue"))
                ).text
            except: telephone = "No telephone number"
            try:
                date = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "prestation_de_sermentValue"))
                ).text
            except: date = "No date"

            #Create a list with the informations about that person
            info = [name, email, adress, postCode, telephone, date]
            #To see collected info in terminal
            print(info)
            # Write the information into row
            thewriter.writerow(info)
            #Go back to main page and repeat the process for next person
            driver.get(f"https://www.avocat-95.fr/recherche-avocat?start={page}")

#The page numbers range to skip next page after finishing collecting all members' information
for x in range(0, 500, 100):
    getInfo(x)
#Quit the chrome driver after completing the task
driver.quit()