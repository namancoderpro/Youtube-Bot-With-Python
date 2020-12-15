import  time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os
import sys
import random
from termcolor import colored
import platform
from colorama import init
import argparse

init()

def driverOS(value):
    version = platform.system()
    options = Options()
    options.headless = value
    if version == "Windows":
        driver = webdriver.Firefox(executable_path="win64/geckodriver.exe", options=options)
    if version == "Linux":
        driver = webdriver.Firefox(executable_path="linux64/geckodriver", options=options)
    if version == "Darwin":
        driver = webdriver.Firefox(executable_path="macos/geckodriver", options=options)

    return driver

def login_gmail(driver, email, passw):
    try:
        #We need this when we work with multiple accounts
        driver.delete_all_cookies()
        url = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dfr%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DUobc1bz8yBQ%2526feature%253Dyoutu.be&hl=fr&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        driver.get(url)
        time.sleep(10)
        #Type the email address
        emailid = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "identifier")))
        emailid.send_keys(email)
        #Click on the next button
        nextButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "identifierNext")))
        ActionChains(driver).move_to_element(nextButton).click().perform()
        #Type the password
        try:
            passwordid = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
            passwordid.send_keys(passw)
        except:
            passwordid = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "password")))
            passwordid.send_keys(passw)
        #Click on the signin button
        signinButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordNext")))
        ActionChains(driver).move_to_element(signinButton).click().perform()
        time.sleep(30)
        driver.get("https://google.com")
        return True
    except:
        return False

#-----------------------Subscribe------------------------------------#
def subscribe(driver, channel):
    try:
        driver.get(channel)
    except:
        print(colored("Please make sure you use the right channel link!", "red"))
    try:
        subscribeButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "subscribe-button")))
    except:
        print(colored("We Couldn't Find The Subscribe Button!", "yellow"))
    if subscribeButton.text == "SUBSCRIBE":
        ActionChains(driver).move_to_element(subscribeButton).click().perform()
    else:
        print("Already Subscribed :)", "blue")

#-----------------------Like------------------------------------#
def like(driver, link):
    try:
        driver.get(link)
    except:
        print(colored("Please make sure you're using a valid link!", "red"))
    likeButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'like this video')]")))
    ActionChains(driver).move_to_element(likeButton).click().perform()
    print(colored(f"{driver.title}: Liked", "green"))

#-----------------------Watch------------------------------------#
def watch(driver, link, delay):
    try:
        driver.get(link)
        time.sleep(3)
    except:
        print(colored("Please enter a valid link!", "yellow"))
    playButton = driver.find_elements_by_xpath("//button[@aria-label='Play']")[0]
    playButton.click()
    #Time in seconds, the video's length
    time.sleep(delay)
    print(colored(f"{driver.title}: Watched", "green"))



def main():
    parser = argparse.ArgumentParser(description="A Youtube Bot Built With Python | It does: Watching, Liking videos & Subscribing to channnels.")
    parser.add_argument("--accounts", type=str, required=True, help="A txt file that holds the gmail accont(s) | [xxxx@gmail.com:password]")
    parser.add_argument("--videos", type=str, required=False, help="A txt file that holds a list of Youtube videos. | [link|length]")
    parser.add_argument("--channels", type=str, required=False, help="A txt file that holds a list of channel(s) links.")
    parser.add_argument("--like",nargs="?",const=True, required=False, help="To like the videos in the list.")
    parser.add_argument("--subscribe",nargs="?",const=True, required=False, help="To subscribe to the channels in the list.")
    parser.add_argument("--watch",nargs="?",const=True, required=False, help="To watch the videos in the list.")

    args = parser.parse_args()
  
    driver = driverOS(False)

    #Open the gmail accounts
    with open(args.accounts, "r") as accountList:
        for account in accountList:
            gmailPassword = account.split(":")
            gmail = gmailPassword[0]
            password = gmailPassword[1]
            #Login
            signin = login_gmail(driver, gmail, password)
            if signin:
                print(colored(f"{gmail}:{password}\tLogin Successfully.", "green"))
                subscribed = False
                #To subscribe
                if args.subscribe:
                    #To avoid unsubscribing
                    if not subscribed:
                        try:
                            with open(args.channels, "r") as channelsList:
                                for channelURL in channelsList:
                                    subscribe(driver, channelURL)
                                    subscribed = True
                        except Exception:
                            print(colored("Make Sure you're using a valid file for the channels list.\nOr Make sure you add ---subscribe."))
                #To watch
                if args.watch:
                    try:
                        with open(args.videos, "r") as videosList:
                            for video in videosList:
                                videoDelay = video.split("|")
                                link = videoDelay[0]
                                delay = int(videoDelay[1])
                                watch(driver, link, delay)
                                #Like the video after watching
                                if args.like:
                                    like(driver, link)
                    except Exception:
                        print(colored("Make Sure you're using a valid file for the videos list.\nOr Make sure you add ---watch."))
                

if __name__ == "__main__":
    main()   

















