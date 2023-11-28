# this function is used to scrape legitimate website from similar web 
# for educational purpose only

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import requests

url_to_capture = 'https://lookerstudio.google.com/reporting/71e3eab6-c7e3-4382-bb69-476655d72a02/page/6zXD'
filename_to_send = 'dashboard'
your_line_token = 'yk6rYeg4y9RncsUNXBqFDAfjRsOJbjwm6EbWzaNev7g'

def capture_screen_url(url, filename):

    driver_dummy = webdriver.Chrome(ChromeDriverManager().install())
    version = driver_dummy.capabilities['chrome']['chromedriverVersion'].split()[0]
    print(version)
    driver = webdriver.Chrome(ChromeDriverManager(driver_version=version).install())
    driver_dummy.quit()

    # print(driver.capabilities)
    # print(driver.capabilities['chrome']['chromedriverVersion'].split()[0])
    driver.get(url_to_capture)
    driver.maximize_window()
    time.sleep(2)

    driver.get_screenshot_as_file("{to_save}.png".format(to_save=filename_to_send))
    driver.quit()

def send_img_to_line(name_of_screen_shot, token=your_line_token, text='Test Image'):
    # much thanks to this medium blog 
    # https://wuttick.medium.com/%E0%B8%AA%E0%B9%88%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1-%E0%B8%9C%E0%B9%88%E0%B8%B2%E0%B8%99-line-notify-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-python-%E0%B9%81%E0%B8%96%E0%B8%A1-code-%E0%B9%81%E0%B8%A5%E0%B8%B0-%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99-894250ca0c52
    
    file_img = {'imageFile': open(name_of_screen_shot, 'rb')}
    # file_img = {'imageFile': open(name_of_screen_shot)}

    # header = {
    #     'content-type':'application/x-www-form-urlencoded',
    #     'Authorization':'Bearer '+ token}

    header = {'Authorization':'Bearer '+ token}
    
    data = "Test from Acha's Laptop"
    
    print(header)

    session_post = requests.post('https://notify-api.line.me/api/notify', headers=header, files=file_img, data= {'message': 'Your Daily Dashboard is here'})
    # session_post = requests.post('https://notify-api.line.me/api/notify', headers=header, files=file_img)
    print(session_post.text)

capture_screen_url(url_to_capture, filename_to_send)
send_img_to_line(name_of_screen_shot='dashboard.png')