from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions 





def launch_android_emulator_driver():
    try:
        cap:Dict[str ,Any]={
            'platformName': 'Android' ,
            "appium:platformVersion": "9" ,
            "appium:deviceName": "emulator-5554" ,
            "appium:udid": "127.0.0.1:5555" ,
            "appium:automationName": "appium" ,
            "appium:systemPort": 8888 ,
            'appium:newCommandTimeout': 0 , 
            'appium:noReset': True ,
            "waitForIdleTimeout": 120000 ,
            "appium:disableWindowAnimation": True ,
            "appium:skipServerInstallation": True ,
            "appium:uiautomator2ServerInstallTimeout": 120000 ,  
            "appium:uiautomator2ServerLaunchTimeout": 240000 , 
            "appium:skipDeviceInitialization": True ,
            "appium:suppressKillServer": True ,
        }


        url = f'http://localhost:4724/wd/hub'

        driver = webdriver.Remote(url , options=AppiumOptions().load_capabilities(cap))
        return driver
    
    except Exception as e:
        return False
