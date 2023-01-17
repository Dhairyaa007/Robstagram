from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

USERNAME = 'Username'
PASSWORD = 'Password'


class RobstaGram:
    def __init__(self):
        self.chrome_driver_path = Service("C://Program Files (x86)/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/')
        self.login()
        self.find_followers()
        self.follow()

    def login(self):
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_btn.click()

    def find_followers(self):
        time.sleep(10)
        self.driver.get("https://www.instagram.com/x_sxls/")

        # time.sleep(3)
        # self.driver.get('https://www.instagram.com/x_sxls/following/')

        time.sleep(5)
        following = WebDriverWait(self.driver,
                                  10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,
                                                                            'following')))
        following.click()

        # time.sleep(10)
        # follow_button = WebDriverWait(self.driver,
        #                               10).until(EC.presence_of_element_located((By.XPATH,
        #                                                                         '/html/body/div[1]/div/div/div/div['
        #                                                                         '2]/div/div/div[1]/div/div['
        #                                                                         '2]/div/div/div/div/div[2]/div/div/div['
        #                                                                         '3]/div[1]/div/div[1]/div['
        #                                                                         '3]/button/div/div')))
        # follow_button.click()

        # time.sleep(5)
        # for run in range(10):
        #     print(f"scrolling down {run}")
        #     self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight'
        #                                , popup)



        # followers.click()
        # scrollbar = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_q/"]/div/div/div/div[2]/div/div/div['
        #                                                '1]/div/div[2]/div/div/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollbar)

    def follow(self):
        time.sleep(5)
        all_following = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'Follow')
        for value in all_following:
            value.click()
            time.sleep(2)


inrob = RobstaGram()
