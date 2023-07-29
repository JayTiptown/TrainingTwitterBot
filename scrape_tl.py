from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
import time
import random

def scrape():

    driver = webdriver.Chrome()

    userTag = driver.find_element(By.XPATH, "//div[@data-testid='User-Names']").text
    timeStamp = driver.find_element(By.XPATH, "//time").get_attribute("datetime")
    tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']").text
    retweet = driver.find_element(By.XPATH, "//div[@data-testid='retweet']").text
    like = driver.find_element(By.XPATH, "//div[@data-testid='like']").text

    UserTags = []
    TimeStamps = []
    Tweets = []
    reTweets = []
    Likes = []

    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    while True:
        for article in articles:
            userTag = driver.find_element(By.XPATH, ".//div[@data-testid='User-Names']").text
            UserTags.append(userTag)

            timeStamp = driver.find_element(By.XPATH, ".//time").get_attribute("datetime")
            TimeStamps.append(timeStamp)

            tweet = driver.find_element(By.XPATH, ".//div[@data-testid='tweetText']")
            Tweets.append(tweet)

            retweet = driver.find_element(By.XPATH, ".//div[@data-testid='retweet']")
            reTweets.append(retweet)

            like = driver.find_element(By.XPATH, ".//div[@data-testid='like']")
            Likes.append(like)

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
        tweetSet = list(set(Tweets))

        if len(tweetSet) > 30:
            break