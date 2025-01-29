import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

today_date = datetime.today().day
today_month_year = datetime.today().strftime("%B %Y")

phone_number_xpath = "//span[contains(.,'Continue with Mobile')]"
Ph_number_field_xpath = "//input[@placeholder='Phone number']"
get_otp_xpath = "//span[normalize-space(text())='Get OTP']"
otp_field_xpath1 = "//input[@id='input-40--0']"
otp_field_xpath2 = "//input[@id='input-40--1']"
otp_field_xpath3 = "//input[@id='input-40--2']"
otp_field_xpath4 = "//input[@id='input-40--3']"
Verify_button_xpath = "//span[normalize-space(text())='Verify']"
testing_institute_text_xpath = "//span[normalize-space(text())='Testing Institute']"
group_courses_xpath = "//span[normalize-space()='Group courses']"
class_xpath = "//a[normalize-space(text())='Classroom for Automated testing']"
place_xpath = "(//div[@class='d-flex align-center']//div)[2]"
start_session = "//span[contains(.,'Start session')]"
presence_of_table_header_xpath = "(//div[@class='v-slide-group__wrapper']//div)[1]"
Lives_sessions_xpath = "(//a[@role='tab'])[2]"
schedule_session_button_xpath = "//button[contains(.,'Schedule sessions')]"
add_session_button_xpath = "//span[contains(.,'Add session')]"
time_picker_xpath = "//div[@aria-owns='list-1937']"
time_xpath = "//div[@id='list-item-1252-40']"
pm_xpath = "(//div[contains(@class,'pa-2 d-flex')])[2]"
create_button = "//button[contains(.,'Create')]"
card_session_name = "(//div[contains(@class,'heading py-10')]//div)[1]"
card_instructor_name = "(//div[contains(@class,'heading py-10')]//div)[2]"
card_upcoming_text = "(//div[@class='text--14 font-weight--500']//span)[3]"
session_time = "(//i[@aria-hidden='true']/following-sibling::div)[1]"

@pytest.fixture()
def setup_and_teatdown():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://staging-web.wise.live")
    driver.maximize_window()
    yield
    driver.quit()
def check_pm(xpath):
    wait = WebDriverWait(driver, 20)
    time.sleep(5)
    text = wait.until(EC.visibility_of_element_located((By.XPATH,xpath))).text
    print(text)
    if text != "PM":
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        time.sleep(4)

def login_with_phn():
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, phone_number_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, Ph_number_field_xpath))).send_keys("1111100000")
    wait.until(EC.element_to_be_clickable((By.XPATH, get_otp_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, otp_field_xpath1))).send_keys("0")
    wait.until(EC.element_to_be_clickable((By.XPATH, otp_field_xpath2))).send_keys("0")
    wait.until(EC.element_to_be_clickable((By.XPATH, otp_field_xpath3))).send_keys("0")
    wait.until(EC.element_to_be_clickable((By.XPATH, otp_field_xpath4))).send_keys("0")
    wait.until(EC.visibility_of_element_located((By.XPATH, Verify_button_xpath))).click()

def test_tc1(setup_and_teatdown):
    wait = WebDriverWait(driver, 20)
    login_with_phn()
    testing_institute_text = wait.until(EC.visibility_of_element_located((By.XPATH, testing_institute_text_xpath)))
    assert testing_institute_text
    Place_text = testing_institute_text.text
    assert Place_text == "Testing Institute"

def test_tc2(setup_and_teatdown):
    wait = WebDriverWait(driver, 20)
    login_with_phn()
    wait.until(EC.element_to_be_clickable((By.XPATH, group_courses_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,class_xpath))).click()
    # assert wait.until(EC.visibility_of_element_located((By.XPATH,class_xpath)))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, place_xpath)))



def test_tc3(setup_and_teatdown):
    wait = WebDriverWait(driver, 20)
    login_with_phn()
    wait.until(EC.element_to_be_clickable((By.XPATH, group_courses_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, class_xpath))).click()
    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.XPATH, Lives_sessions_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, schedule_session_button_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, add_session_button_xpath))).click()
    time.sleep(5)
    check_pm(pm_xpath)
    time.sleep(3)
    wait.until((EC.element_to_be_clickable((By.XPATH, create_button)))).click()

def test_tc4(setup_and_teatdown):
    wait = WebDriverWait(driver, 20)
    login_with_phn()
    wait.until(EC.element_to_be_clickable((By.XPATH, group_courses_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, class_xpath))).click()
    print("class xpath")
    assert wait.until(EC.visibility_of_element_located((By.XPATH, card_session_name)))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, card_instructor_name)))
    text = wait.until(EC.visibility_of_element_located((By.XPATH, card_upcoming_text))).text
    assert text == "Upcoming"
    assert wait.until(EC.visibility_of_element_located((By.XPATH, session_time)))