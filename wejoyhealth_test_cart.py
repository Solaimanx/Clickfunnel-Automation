from selenium import webdriver
from time import sleep
import pickle


# define the web driver
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')
driver.implicitly_wait(40)


def main():

    for i in range(50):
        url = 'https://wejoyhealth.com/products/shop-wejoybalance'
        driver.get(url)
        sleep(9)
        button = driver.find_element_by_class_name('custom_atc')
        button.click()
        cart = driver.find_element_by_xpath('//*[@id="cartform"]/div[1]/div[1]/div[1]/a')
        cart.click()
        sleep(5 )
        working_url = driver.current_url
        url__  = 'https://wejoyhealth.com/cart'

        if(working_url == url__):
            print('working',i)
        else:
            print('error found ',i)


main()

