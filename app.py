from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys



class bot:
    def __init__(self, username, password, user, message):
        self.username = 'thomas.exe._'
        self.password = 'Muppet2006'
        self.user = 'ralucapopp'
        self.message =  'This is an automated message. If you recieve this message, Toma is a great programmer.<3'
        self.base_url = 'https://www.instagram.com/'
        self.bot = webdriver.Chrome("C:/chromedriver.exe")
        self.login()



        


    def login(self):
        self.bot.get(self.base_url)
        
        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
        self.bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(4)
        self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(self.user)
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
        time.sleep(2)
        self.bot.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(self.message)
        time.sleep(1)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

def init():     
    bot('thomas.exe._', 'Muppet2006', 'poppraluca', 'This is an automated message. If you recieve this message, Toma is a great programmer.<3' )
    input("DONE")

init()
