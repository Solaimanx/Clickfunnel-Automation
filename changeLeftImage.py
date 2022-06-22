from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os
import pickle
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.support.ui import Select


# define the web driver
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')
driver.implicitly_wait(5)

#veriables to track activity in terminal

link_list = []

footer_found = 0
footer_didnt_found = 0
logo_found = 0
logo_didnt_found = 0
seo_not_found = 0
seo_found = 0
total = 0
no = 0
new_logo = 0 
new_logo_not = 0



username ='username'
password = 'password'



#get cookis from website
def get_cookies():
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="user_remember_me"]').click()
    driver.find_element_by_xpath('//*[@id="loginfields"]/div[4]/input').click()
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    print('store the chookies successfully')
    sleep(8)
    driver.find_element_by_xpath('//a[contains(text(),"Got it!")]').click()



#login 
def login_with_cookies():
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    print('login successfully')
    sleep(4)
    driver.find_element_by_xpath('//a[contains(text(),"Got it!")]').click()





def change_image(link):
    global logo_found
    global logo_didnt_found
    global new_logo
    global new_logo_not

    driver.get(link)
    #Click "edit Page"
    sleep(5)
    wait = WebDriverWait(driver,15)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'btn btn-warning openPageInEditor')])[1]")))
    driver.execute_script("arguments[0].click()",next_button)
    sleep(9)

    try:
        #click on newLogo
        newlogo1 = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/77/ed40866d314783bde08dd7c5fbee1e/logowithshadow-150px.png')]")
        newlogo1.click()
        #click on advance settings
        advance_settings1 = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings1.click()
        #image input field

        # clean image width and set lazy loading to false
        img_width_input1 = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[3]/input')
        sleep(1)
        img_width_input1.clear()
        sleep(1)
        select1 = Select(driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[7]/select'))
        select1.select_by_value('false')

        #close settings and Save

        sleep(1)
        driver.find_element_by_xpath('/html/body/div[11]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
        new_logo += 1
        sleep(6)
        
    except:
        new_logo_not +=1

            

    try:
        #white logo
        logo2 = driver.find_element_by_xpath("//div[contains(@style,'https://images.clickfunnels.com/09/27146ca7a14860a8c3ae2fbf29c85c/arnold-w-white-text-sss.png')]")
        logo2.click()
        sleep(1)
        
        # open settings for editing background image 
        open_right_popup = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools-row ')][contains(@style,'block')]/div[2]/div[1]")
        open_right_popup.click()

        #backgroundimage input field
        sleep(1)
        img_input2 = driver.find_element_by_xpath('//div[contains(@class,"editorSectionGroup clearfix eTabs_settings")][1]/input')
        sleep(1)
        img_input2.clear()
        sleep(1)
        img_input2.send_keys('https://images.clickfunnels.com/25/87f1f0047a4fafac1beba3c351b4b7/arnold-w-white-text-sss.png')


        sleep(1)
        driver.find_element_by_xpath('/html/body/div[11]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
        sleep(6)

        logo_found += 1
    except:
        logo_didnt_found += 1



def main():
    global total
    # get_cookies()
    login_with_cookies()
    # collect_all_link()
    
    f = open('data4.json')
    links = json.load(f)

    
    # try:
    #     link_list.remove('https://infoa9bf3f-app.clickfunnels.com')
    # except:
    #     sleep(1)


    # with open('data.json','w') as f:
    #     json.dump(link_list,f)

    for page_link in links:
        change_image(page_link)
        print(page_link)
        print('data4')
        total += 1
        print('_____________________________________________')
        print('Pages check done =======>  '+ str(total))

        print('SEO added =====> '+str(logo_found)+ '\n' +'SEO not found  =====> '+str(logo_didnt_found) + '\n'+ 'footer added =====> '+str(new_logo)+'\n'+ 'Foodter didn\'t found  =====> '+ str(new_logo_not))



#start here
main()
