import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

delay = 3  # seconds
test_email = 'test@test.com'
test_password = 'test1234'

def init_browser():
    if os.name == 'nt':
        return webdriver.Chrome()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        return webdriver.Chrome(options=chrome_options)


def test_correct_login():
    driver = init_browser()
    driver.get("https://homeemity.com/login/")
    driver.find_element_by_name('uemail').send_keys(test_email)
    driver.find_element_by_name('upassword').send_keys(test_password + Keys.RETURN)

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'success')))
        output_text = driver.find_element_by_class_name("success")
        assert output_text.text == "Login successful"
    except TimeoutException:
        assert False

    driver.close()


def test_incorrect_login():
    driver = init_browser()
    driver.get("https://homeemity.com/login/")
    driver.find_element_by_name('uemail').send_keys(test_email)
    driver.find_element_by_name('upassword').send_keys('wrong_password' + Keys.RETURN)

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'alert')))
        output_text = driver.find_element_by_class_name("alert")
        assert output_text.text == "Email or password is incorrect"
    except TimeoutException:
        assert False

    driver.close()
