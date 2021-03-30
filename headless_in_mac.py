from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1700,1000")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver',options=chrome_options)
driver.implicitly_wait(25)


#code start here


def main():
    driver.get("https://google.com")
    driver.save_screenshot("screenshot.png")
    print("done in headless mode")


main()