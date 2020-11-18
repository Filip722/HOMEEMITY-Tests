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


def test_incorrect_link_address():
    driver = init_browser()
    driver.get(
        "https://homeemity.com/login/link?client_id=1jdlmc3j63589h2mbj5cvshn0i&response_type=code&state=A2SAAEAEM4WeeuOu1IYWs_e7WEuy1oCEMyGj1GVaxdndpz5qHWdeHE1oPYyFLN0f_N6aTO0D2__5YvEGL7oBoKkg21trtNQH06qc25kxUlw1Tch8-LOxMGoqmVCAydmNuDmYYc59M_tWMUBKIj6Yk7CIcglJbARZWb6uIeMJKCM78tcpJOYyhP4VQg5fH1h9Bx51Y-81ypq3FFv6EboyNXM6VmeYJ8RErQZb3sujgpFJnT-K-ttVN46jeexKKMB8u1ZeHkcfI7YE3Ki8ZLwtMs8qFAt4jXoQW5NLyeRxFDjRX28ekjy74ptHsVJps2dp4lJ2u1UDLm4LYTmKseluvcgHnX06RPPT9p_ejRRVHnRpL53etyfJ1EQPDF-sPjmherMr0lk1kn5AIpFTPnF3Qt2z4twgpKa51N408QGU8qOy4Nlf3Xsr4T91k5q3Wd7naCqwuQzqTlYlGxtsk_QMnIBgLExBj4_cpX1_gJtOcERzsKGGO5l1HqBZDz3T09efIntXxfvBFVuqaV1rzgDURjnm0bK08DfNuvqlGjZnjtw-NU1wlgHpiWwuYsXcFsuXx10ra3MUCGFgJp1nFu0T4R97QgYSf8MxJcXotHdkpMzVCK1lD0TQjqVp8txEuLXnRSQlQP-AoF0F6pLGpH-aio5lGWg9FmZCOd_fCSYFznkt4oP1wJeJ8W1_NGUkzmJLQ6GNGhgIkK7ruD5AlaWu8fY71x7fEmjaw&scope=openid%20profile&redirect_uri=https%3A%2F%2Fpitangui.amazon.com%2Fapi%2Fskill%2Flink%2FM22Q86CT67KF9B&fbclid=IwAR2Y9cIp6lhqMjqmNt-HeIdnmEluTvyc_1gXBM16aRob8YMAYGlRLpMhk_s")
    driver.find_element_by_name('uemail').send_keys(test_email)
    driver.find_element_by_name('upassword').send_keys(test_password + Keys.RETURN)

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-spacing-small')))
        output_text = driver.find_element_by_class_name("a-spacing-small")
        assert output_text.text == "Linking unsuccessful."
    except TimeoutException:
        assert False

    driver.close()
