from multiprocessing.pool import Pool
import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import time , sys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from launch_android_emulator_driver import launch_android_emulator_driver
from operations import Operations
from authenticate_gmail import authentication
import argparse


def start_automation():
    parser = argparse.ArgumentParser(description="start authentication process")
    parser.add_argument("--email", help="Gmail email")
    parser.add_argument("--password", help="Gmail password")
    args = parser.parse_args()

    if args.email and args.password:
        print(f"Starting automation with email: {args.email}")
    else:
        print("Please provide a email and password.")

        
    driver = launch_android_emulator_driver()

    if driver == False:
        print('Could not start automation') 
        return
    
    res = Operations(driver).add_proxy()

    if res == False:
        return

    Operations(driver).reset_google_apps()
    start_auth = authentication(driver, args.email, args.password ).start_authentication()

    if start_auth :
        print ("Authentication successful")
    else :
        print ("Authentication failed")




if __name__ == "__main__":
    start_automation()