from selenium import webdriver
from time import sleep
import pickle


# define the web driver
options = webdriver.ChromeOptions() 
options.add_argument("window-size=1200x800")
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')
driver.implicitly_wait(10)

username = 'username'
password = 'password'

def get_cookies():
    driver.get('https://www.quiz-maker.com/Account-Login')
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/input[1]').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/input[1]').send_keys(username)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/input[2]').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/input[2]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="ul-btn-1"]').click()
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    print('chookies collected')
    driver.get('https://www.quiz-maker.com/Dashboard')
    sleep(9)

def login_with_cookies():
    driver.get('https://www.quiz-maker.com/Dashboard')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://www.quiz-maker.com/Dashboard')
    print('login sucess')



def add_plugin():
    for i in range(36,40):
        print(i)
        driver.get('https://www.quiz-maker.com/Dashboard')
        sleep(8)
        driver.find_element_by_xpath('//*[@id="rqlSearch"]').click()
        driver.find_element_by_xpath('//*[@id="rqlSearch"]').send_keys('american')
        sleep(7)
        driver.execute_script('document.querySelector("#main").scrollTo(0,1000)')
        sleep(4)
        driver.execute_script('document.querySelector("#main").scrollTo(1000,2500)')
        sleep(4)
        driver.execute_script('document.querySelector("#main").scrollTo(2500,3500)')
        driver.execute_script('document.querySelector("#main").scrollTo(2500,4500)')
        driver.execute_script('document.querySelector("#main").scrollTo(2500,5500)')
        sleep(5)
        title = 'document.querySelector("#dashboard_table > div.table-box > div.table-tr > div:nth-child({}) > div:nth-child(1)").click()'.format(i)
        driver.execute_script(title)
        sleep(7)
        driver.switch_to.frame(0)
        driver.find_element_by_xpath('//*[@id="quiz-maker"]/div[1]/div[4]').click()
        sleep(6)
        driver.find_element_by_xpath('//*[@id="score-tabs"]/div[1]/div[8]/div[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="rtilesWin"]/div/div[5]/div[12]/div[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="rtilesWin"]/div/div[6]/a[1]').click()
        sleep(4)
        driver.find_element_by_xpath('//*[@id="quiz-save"]').click()
        sleep(5)
        





get_cookies()
# login_with_cookies()e
add_plugin()
