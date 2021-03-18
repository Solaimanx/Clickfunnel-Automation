from selenium import webdriver
from time import sleep
import pickle


# define the web driver
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')
driver.implicitly_wait(40)

# login credentials
username ='info@ericniceberg.com'
password = 'xJL3E6PJCQkj3yx'

all_links = []

#get cookis from website
def get_cookies_():
    driver.get('https://app.clickfunnels.com/users/sign_in')
    driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="user_remember_me"]').click()
    driver.find_element_by_xpath('//*[@id="loginfields"]/div[4]/input').click()
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    print('store the chookies successfully')


#login 
def login_with_cookies():
    driver.get('https://app.clickfunnels.com/users/sign_in')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://infoa9bf3f-app.clickfunnels.com/members?page_id=33523349')
    sleep(25)
    print('login successfully')

#collect all the links from every page
def collect_links():
    global all_links
   # Acceept terms and conditions
    sleep(10)
    try :
        driver.find_element_by_xpath('//a[contains(text(),"Got it!")]').click()
    except:
        print("Not able to click on |Got it|")
     #first page data collection
    contact = driver.find_elements_by_xpath('//a[contains(text(),"Edit")]')
    for every_contact in contact:
        new_link = every_contact.get_attribute("href")
        all_links.append(new_link)
    #loop all the page 
    i = 1
    #correct one while i <8
    while i <10:
        sleep(7)
        try:
            driver.find_element_by_xpath('//a[contains(text(),"Next")]').click()
        except:
            print('last next click')
        sleep(10)
        contact = driver.find_elements_by_xpath('//a[contains(text(),"Edit")]')
        for every_contact in contact:
            new_link = every_contact.get_attribute("href")
            all_links.append(new_link)
        i += 1
        print(i)
        
    print(len(all_links))
    print('collected all the links')
    return

#add the specific tag to contact
def add_tags():
    i = 0
    for onelink in all_links:
        url = onelink
        driver.get(url)
        i += 1
        print(i)
        sleep(10)
        driver.find_element_by_xpath('//*[@id="quick-actions-dropdown"]').click()  
        sleep(9)  
        driver.find_element_by_xpath('//*[@id="add-tags"]').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="add-tags-form"]/div/div/input').send_keys('basic')
        sleep(2)
        driver.find_element_by_xpath('//div[contains(@class,"item selected")]').click()
        sleep(2)
        driver.find_element_by_xpath('//div[contains(@class,"ui fluid search dropdown select select optional selection multiple active visible")]/i').click()
        sleep(9)
        driver.find_element_by_xpath('//div[@id="add-tags-modal"]/div/div/div[4]/div/div[2]').click()

    return

def main():
    #get_cookies_()
    login_with_cookies()
    collect_links()
    add_tags()



# start the Script
main()