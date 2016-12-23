from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def get_firefoxbinary():
    return FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox')

binary = get_firefoxbinary()
driver = webdriver.Firefox(firefox_binary=binary)
driver.get("http://127.0.0.1:8000/")
assert "Django" in driver.title