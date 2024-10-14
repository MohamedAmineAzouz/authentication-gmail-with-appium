
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By




class authentication():
    
    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password




    async def start_authentication(self):
        start_app = self.start_app_gmail()
        if not start_app :
            return False
        
        insert_email = await self.insert_email()
        if not  insert_email :
            return False
        
        insert_password = await self.insert_password()
        if not insert_password :
            return False
        
        return True


    async def start_app_gmail(self):
        try:
            await asyncio.sleep(5)
            WebDriverWait(self.driver, 50).until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID  ,"Gmail" )).click()
            print("application gmail is running")
            await asyncio.sleep(5)

            await self.click_button_compose()
            await self.handle_welcome_tour()

            self.driver.press_keycode(59, metastate=1)  # 59 is the key code for "Shift"
            self.driver.press_keycode(61)  # 61 is the key code for "Tab"
            await asyncio.sleep(0.5)
            self.driver.press_keycode(59, metastate=1)
            self.driver.press_keycode(61)

            WebDriverWait(self.driver, 50).until(lambda x: x.find_element(By.ID ,'com.google.android.gm:id/setup_addresses_add_another')).click()
            print("button add an email address has been clicked")
            await asyncio.sleep(2)

            WebDriverWait(self.driver, 50).until(lambda x: x.find_element(By.XPATH ,"//android.widget.LinearLayout[@resource-id='com.google.android.gm:id/account_setup_item']")).click()
            print("button Google has been clicked")
            await asyncio.sleep(5)
            return True
        
        except Exception as e:
            raise e




    async def handle_welcome_tour(self):
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element(By.ID ,'com.google.android.gm:id/welcome_tour_got_it')).click()
            print("button GOT IT has been clicked")
            await asyncio.sleep(1)
        except:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element(By.ID ,'com.google.android.gm:id/welcome_tour_skip')).click()
            print("button skip has been clicked")
            await asyncio.sleep(1)



    async def click_button_compose(self):
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element(By.XPATH ,'//android.widget.TextView[@content-desc="Compose"]')).click()
        except:
            pass


    async def insert_email(self):
        try:
            input_email = WebDriverWait(self.driver, 180).until(lambda x: x.find_element(By.XPATH ,'//android.widget.EditText[@resource-id="identifierId"]'))
            await asyncio.sleep(15)
            input_email.send_keys( self.email )
            print("email has been inserted successfully")
            await asyncio.sleep(5)

            WebDriverWait(self.driver, 50).until(lambda x: x.find_element(By.XPATH ,'//android.widget.Button[@text="Next"]')).click()
            print("button Next has been clicked")
            await asyncio.sleep(20)

            return True
        
        except Exception as e:
            print("input email not found")


    async def insert_password(self):
        try:
            insert_pass = await self.insert_password_in_input()
            if not insert_pass:
                raise 'input password not found'

            WebDriverWait(self.driver, 50).until(lambda x: x.find_element(By.XPATH ,'//android.widget.Button[@text="Next"]')).click()
            print("button Next has been clicked")
            await asyncio.sleep(25)

            try:
                error = WebDriverWait(self.driver, 15).until(lambda x: x.find_element(By.XPATH ,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.TextView"))
                print(error.get_dom_attribute("text"))
                return False
            except:
                pass

            print("authentication successful")
            return True
            
        except:
            print("input password not found something went wrong")
            return False


    async def insert_password_in_input( self ):
        try:
            input_password = WebDriverWait(self.driver, 60).until(lambda x: x.find_element(By.XPATH ,'//android.view.View[@resource-id="password"]/android.view.View/android.view.View/android.widget.EditText'))
            await asyncio.sleep(15)
            input_password.send_keys(self.data.email_password)
            print("password has been inserted successfully")
            await asyncio.sleep(2)
            return True
        
        except:
            return False
