from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')

driver.get("https://www.yelp.com/search?find_desc=coach&find_loc=San+Francisco%2C+CA&ns=1")
wait = WebDriverWait(driver, 10)


i = 0
while i < 10:
    element = wait.until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[24]/div/div[1]/div/div[11]/span/a'))
    )
    element.click()
    print(i)
    i += 1







