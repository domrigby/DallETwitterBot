from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import os


class ImageMaker():

    def __init__(self,text):

        self.text = text

        self.createImage()
        self.waitForImage()
        #self.findImage()

        self.driver.close()

    def createImage(self):

        self.driver = webdriver.Firefox(executable_path="./selenium_firefox/drivers/geckodriver")

        self.driver.get("https://www.craiyon.com/")

        self.driver.maximize_window()

        self.driver.execute_script("window.scrollTo(0, 350)") 


        ## must wait for privacy warning

        time.sleep(4)

        try:
            print("Waiting for privacy warning")
            element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class=' css-b2i6wm'])[2]")))
            self.driver.find_element(By.XPATH,"(//button[@class=' css-b2i6wm'])[2]").click()
        
        except:
            print("no privacy warning")

        print(self.driver.title)

        self.text_enter = self.driver.find_element(By.ID,"prompt")

        print(self.text)

        self.text_enter.send_keys(self.text)

        self.text_enter.send_keys(Keys.RETURN)


    def waitForImage(self):
        try:
            element = WebDriverWait(self.driver, 150).until(
            EC.presence_of_element_located((By.XPATH,"(//img[contains(@class,'h-full w-full')])[1]")))    #By.ID, "aniplayer"))
            print("Image detected")

        except Exception as e:
            print("Failed to produce image")
            print(e)
            self.driver.quit()

        #self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/main[1]/div[3]/div[1]/button[1]/span[1]").click() 
        #print("Image download started")

        self.tag = self.text.replace(" ","_")
        self.tag = "images_generated/"+self.tag+".png"
        self.driver.save_screenshot(self.tag)

    def deleteImage(self):
        file_path = self.tag
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File has been deleted")
        else:
            print("File does not exist")
        








