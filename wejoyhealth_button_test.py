from selenium import webdriver
from time import sleep
import pickle


# define the web driver
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')
driver.implicitly_wait(40)


def main():

    for i in range(40):
        url = 'https://wejoyhealth.com/products/shop-wejoybalance'
        driver.get(url)
        sleep(10)
        one_time = driver.find_element_by_xpath('//*[@id="prizebox"]/label[2]/div/span')
        one_time.click()
        dropdown = driver.find_element_by_class_name('pf-variant-select')
        dropdown.send_keys('1 Bottle -  $49.00 ')
        add_to_cart = driver.find_element_by_xpath('//*[@id="addtoartb"]')
        add_to_cart.click()
        sleep(8)
        print(i,'1bottle')

    
    for i in range(40):
        url = 'https://wejoyhealth.com/products/shop-wejoybalance'
        driver.get(url)
        sleep(10)
        one_time = driver.find_element_by_xpath('//*[@id="prizebox"]/label[2]/div/span')
        one_time.click()
        dropdown = driver.find_element_by_class_name('pf-variant-select')
        dropdown.send_keys('3 Bottles -  $129.00 ')
        add_to_cart = driver.find_element_by_xpath('//*[@id="addtoartb"]')
        add_to_cart.click()
        sleep(8)
        print(i,'3bottle')

    for i in range(40):
        url = 'https://wejoyhealth.com/products/shop-wejoybalance'
        driver.get(url)
        sleep(10)
        one_time = driver.find_element_by_xpath('//*[@id="prizebox"]/label[2]/div/span')
        one_time.click()
        dropdown = driver.find_element_by_class_name('pf-variant-select')
        dropdown.send_keys('6 Bottles -  $246.00 ')
        add_to_cart = driver.find_element_by_xpath('//*[@id="addtoartb"]')
        add_to_cart.click()
        sleep(8)
        print(i,'6bottle')



main()

