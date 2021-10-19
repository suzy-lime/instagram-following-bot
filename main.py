from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

# CONSTANTS
USERNAME = os.environ.get("SECRET_USER")
PASSWORD = os.environ.get("SECRET_PASSWORD")
ACCOUNT = os.environ.get("SECRET_ACCOUNT")
CHROME_DRIVER_PATH = "C:/Users/ccesports2/Development/chromedriver"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()

        time.sleep(3)

        user_input = self.driver.find_element_by_name("username")
        user_input.send_keys(USERNAME)
        pass_input = self.driver.find_element_by_name("password")
        pass_input.send_keys(PASSWORD)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        print("logged in")

        time.sleep(3)

    def find_followers(self):
        not_now = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now.click()

        time.sleep(1)

        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/?hl=en")
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(3)
        pop_up = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for x in range(10):

            try:
                self.follow()
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                continue

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            time.sleep(2)

    def follow(self):
        follower_list = self.driver.find_elements_by_xpath('//button[text()="Follow"]')
        for follower in follower_list:
            follower.click()



insta_bot = InstaFollower()

insta_bot.login()

insta_bot.find_followers()

# insta_bot.follow()
