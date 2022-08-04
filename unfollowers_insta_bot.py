from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from credentials import un, pw
import time


def initialise_driver(link):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("chromedriver",options=options)
    driver.get(link)
    time.sleep(5)
    return driver


#logs into instagram account
def insta_login(driver, username, password):
    try:
        # Entering username
        username_box = driver.find_element(By.XPATH, "//input[@name = 'username']")
        username_box.send_keys(username)
        time.sleep(2)

        # Entering password
        password_box = driver.find_element(By.XPATH, "//input[@name = 'password']")
        password_box.send_keys(password)
        time.sleep(2)

        login_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Log In')]")
        login_button.click()
        time.sleep(2)
        print(f"{username} logged in successfully")

        time.sleep(15)
    except:
        print(f"{username} log in failed...")
        print("Please try again")

    try:
        not_now_button = driver.find_element(By.XPATH, "//button[text() = 'Not Now']")
        not_now_button.click()
    except:
        pass

    time.sleep(15)

    try:
        not_now_button = driver.find_element(By.XPATH, "//button[text() = 'Not Now']")
        not_now_button.click()
    except:
        pass

    time.sleep(2)


#opens instagram profile if already logging in
def go_to_insta_profile(driver):
    try:
        avatar_button = driver.find_element(By.XPATH, "//span[@class ='_aa8h _aa8i']")
        avatar_button.click()

        time.sleep(2)

        profile_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Profile')]")
        profile_button.click()

    except:
        print("Profile button not located, please try again")

    time.sleep(5)


def get_list(driver, button_xpath):
    l = []
    button = driver.find_element(By.XPATH, button_xpath)
    if "followers" in button_xpath:
        count = button.get_attribute('title')
    else:
        count = button.text
    button.click()

    loops_count = (int(count) // 12)
    # loops_count = int(count)
    time.sleep(9)

    list_ul = driver.find_element(By.XPATH, "//div[@class='_aae-']")

    time.sleep(5)

    for i in range(loops_count):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", list_ul)
        time.sleep(8)
        users_div = list_ul.find_elements(By.TAG_NAME, "li")
        for us in users_div:
            us = us.find_element(By.TAG_NAME, "a").get_attribute("href")
            us1 = us.replace("https://www.instagram.com/", "")
            us = us1.replace("/", "")
            l.append(us)
        time.sleep(4)

    time.sleep(20)
    close = driver.find_element(By.CSS_SELECTOR, "div[class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _ab9y _abcm']>button")
    close.click()
    time.sleep(7)

    return l


url_ = "https://www.instagram.com/accounts/login/"
followers_button_xpath = "//div[contains(text(), 'followers')]/span"
following_button_xpath = "//div[contains(text(), 'following')]/span"

driver = initialise_driver(url_)
insta_login(driver, un, pw)
go_to_insta_profile(driver)
followers_list = get_list(driver, followers_button_xpath)
following_list = get_list(driver, following_button_xpath)

driver.quit()

unfollowers = []
for profile in following_list:
    if profile not in followers_list:
        unfollowers.append(profile)


print("The unfollowers list is:")
print(unfollowers)