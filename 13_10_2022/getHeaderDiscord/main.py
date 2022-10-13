# Import the required modules
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from selenium.webdriver.chrome.service import Service
  

if __name__ == "__main__":
  

    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
    
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    options = webdriver.ChromeOptions()

    options.add_argument("disable-gpu")
    options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    
    options.add_argument("--ignore-certificate-errors")
    options.add_argument(r"--user-data-dir=C:\Users\ADMIN\Desktop\getheadersele\profileTest")
    
    driver = webdriver.Chrome(service=Service(r"C:\Users\ADMIN\Desktop\getheadersele\chromedriver.exe"
        ),
                              options=options,
                              desired_capabilities=desired_capabilities)
  
    driver.get("https://discord.com/channels/@me")
  

    logs = driver.get_log("performance")
    for log in logs:
        network_log = json.loads(log["message"])["message"] 
        a =  network_log["params"]
        if a.get('headers') != None:
            if a.get('headers').get('authorization') != None:
                print(a.get('headers').get('authorization'))
                break
    driver.quit()
  
