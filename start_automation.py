import asyncio
from launch_android_emulator_driver import launch_android_emulator_driver
from operations import Operations
from authenticate_gmail import authentication
import argparse


async def start_automation():
    parser = argparse.ArgumentParser(description="start authentication process")
    parser.add_argument("--email", help="Gmail email")
    parser.add_argument("--password", help="Gmail password")
    args = parser.parse_args()

    if args.email and args.password:
        print(f"Starting automation with email: {args.email}")
    else:
        print("Please provide a email and password.")

        
    driver = await launch_android_emulator_driver()

    if driver == False:
        print('Could not start automation') 
        return
    
    res = await Operations(driver).add_proxy()

    if res == False:
        return

    await Operations(driver).reset_google_apps()
    start_auth = await authentication(driver, args.email, args.password ).start_authentication()

    if start_auth :
        print ("Authentication successful")
    else :
        print ("Authentication failed")




if __name__ == "__main__":
    asyncio.run(start_automation())