from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from dotenv import load_dotenv
import time
import random
import os

def logInPath():
    backspace_weights = [98, 2]
    backspace_exec = 1

    load_dotenv()

    from_user = os.getenv("TWIT_USERNAME")
    from_pass = os.getenv("TWIT_PASSWORD")
    
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/i/flow/login") #Switch to http://www.x.com if necessary

    time.sleep(random.uniform(1.0, 5.0)) #randomized timings for actions to avoid bot detection <-- I love copilot bruh. this just saved me so much typing

    username = driver.find_element(By.XPATH, "//input[@name='text']")
    user_creds = from_user
    for letter in user_creds:
        username.send_keys(letter)
        time.sleep(random.uniform(0.1, 0.5))
        if (random.choices(backspace_weights, weights = [98, 2]) == backspace_exec):
            username.send_keys(Keys.BACKSPACE)
            time.sleep(random.uniform(0.1, 0.5))

    time.sleep(random.uniform(1.0, 5.0))

    next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
    next_button.click()

    time.sleep(random.uniform(1.0, 5.0))
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    pass_creds = from_pass

    for letter in pass_creds:
        password.send_keys(letter)
        time.sleep(random.uniform(0.1, 0.5))
        if (random.choices(backspace_weights, weights = [98, 2]) == backspace_exec):
            password.send_keys(Keys.BACKSPACE)
            time.sleep(random.uniform(0.1, 0.5))

    log_in_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")
    log_in_button.click()


    # while (True): #KEEP: meant to keep the program running until the user exits
    #     pass