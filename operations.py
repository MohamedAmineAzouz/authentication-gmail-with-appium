




class Operations():

    def __init__(self, driver):
        self.driver = driver



    def add_proxy( self ):
        proxy_ip = "111.111.111.111"
        proxy_port = "8080"
        command =  f"""
                        settings put global http_proxy {proxy_ip}:{proxy_port};
                        settings put global global_http_proxy_host {proxy_ip};
                        settings put global global_http_proxy_port {proxy_port};
                    """
        
        try:
            res = self.driver.execute_script("mobile: shell", {
                "command": command,
                "includeStderr": True,
                "timeout": 15000
            })

            print(f"Proxy setup result: {res}")
            return True
        
        except Exception as e:
            print(f"An error occurred while setting the proxy: {e}")
            return False
        

    def reset_google_apps ( self ):
        try:
            res =  self.driver.execute_script('mobile: shell',{
                "command": "pm  list packages | grep com.google | sed 's/package://' | while read i; do pm clear $i ; done",
                "includeStderr": True,
                "timeout": 15000
            })

            print(f"Reset Google apps result: {res}")
            
        except Exception as e:
            print(f"An error occurred during the Google apps reset: {e}")