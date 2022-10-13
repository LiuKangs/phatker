
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import os , re

from imap_tools import MailBox, AND
from time import sleep



def makeDriver():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    userdatadir = f'{os.path.join(ROOT_DIR, f"dlkjsksd")}'

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument(f"--user-data-dir={userdatadir}")

    chromeOptions.add_experimental_option("detach", True)
    chromeOptions.add_argument("disable-gpu")
    chromeOptions.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chromeOptions)

    return driver





def getMailCode(mail):
    '''
    hàm ``getMailCode()`` dùng để lấy về đối tượng mail chưa đọc
    
    (mail : mail cần lấy code)
    
    - Dữ liệu trả về là opcode hoặc None
    - Nếu không tìm thấy tin nhắn mới sẽ trả về None
    '''
    imap_host = 'mail.maxbulon.com'
    imap_user = '_mainaccount@maxbulon.com'
    imap_pass = 'Nguyenhoanganh2004@'


    while True :
        with MailBox(imap_host).login(imap_user, imap_pass, 'INBOX') as mailbox:
            for msg in mailbox.fetch(AND(seen=False)):
                body = msg.text
                if body.find(mail) != -1:
                    otp_code = findOtpCode(body)
                    if otp_code != None:
                        return otp_code[0]
                    break
        sleep(2)


def findOtpCode(msg:str) -> list:
    '''
    hàm ``findOtpCode`` dùng để tìm otp code từ msg tham số
    dữ liệu trả về kiểu list nếu tìm thấy code và None nếu không tìm thấy
    ## exam :
    ``` python
        msg = "code của bạn là 00000"
        r = findOtpCode(msg)
    ```
    '''
    
    compile = '[0-9]{4,8}.(?=)?'
    r =  re.findall(compile,msg)
    if len(r) > 0:
        return r
    else:
        return None



def setForwardImap(driver):
    driver.get('https://mail.google.com/mail/u/0/#settings/fwdandpop')
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='button'][act='add']")))
    els.click()
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text'][size='48']")))
    els.send_keys("maxbulon@maxbulon.com")
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[name='next']")))
    els.click()
    
    current_page = driver.current_window_handle
    newPopup = driver.window_handles[-1]
    
    driver.switch_to.window(newPopup)
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='submit']")))
    els.click()
    
    driver.switch_to.window(current_page)
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[name='ok']")))
    els.click()
    
    
    
    
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text'][act='verifyText']")))
    els.clear()
    otp_ = getMailCode('nhatminhlatao7@gmail.com')
    els.send_keys(otp_)
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='button'][act='verify']")))
    els.click()
    
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='radio'][value='1']")))
    els.click()
    
    els = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[guidedhelpid='save_changes_button']")))
    els.click()






   
# setForwardImap(driver)



# test get newmail

driver = makeDriver()

setForwardImap(driver)
            