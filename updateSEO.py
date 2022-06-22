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



def seo_meta_tag(link):
    global seo_found
    global seo_not_found

    driver.get(link)
    #Click "edit Page"
    sleep(5)
    wait = WebDriverWait(driver,15)



    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'btn btn-warning openPageInEditor')])[1]")))
    driver.execute_script("arguments[0].click()",next_button)
    sleep(8)

    try:
        #check if there are any logo
        settings = driver.find_element_by_xpath('//*[@id="editorTopNav_settings"]')
        hover_settings = ActionChains(driver).move_to_element(settings)
        hover_settings.perform()
        sleep(1)
        #click on settings > Seo meta data
        nav_bar = driver.find_element_by_xpath('//*[@id="editorTopNav_settings"]/div/div[2]')
        ActionChains(driver).move_to_element(nav_bar).perform()
        driver.execute_script("arguments[0].click()",nav_bar)
        sleep(4)
        #meta data
        pyperclip.copy('FLOW פשוט לדבר אנגלית')  
        seo_meta_data = driver.find_element_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div[3]/input')
        seo_meta_data.clear()
        driver.execute_script("arguments[0].click()",seo_meta_data)
        seo_meta_data.send_keys(Keys.COMMAND, 'v')
        sleep(2)
        #description
        pyperclip.copy('FLOW פשוט לדבר אנגלית')  
        seo_description = driver.find_element_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div[4]/textarea')
        seo_description.clear()
        driver.execute_script("arguments[0].click()",seo_description)
        seo_description.send_keys(Keys.COMMAND, 'v')
        sleep(2)
        #keywards
        pyperclip.copy('FLOW פשוט לדבר אנגלית')  
        seo_keywards = driver.find_element_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div[5]/input')
        seo_keywards.clear()
        driver.execute_script("arguments[0].click()",seo_keywards)
        seo_keywards.send_keys(Keys.COMMAND, 'v')
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[11]').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
        seo_found += 1
        sleep(6)
    except:
        seo_not_found += 1
        print('don\'t have seo option ')





def change_image(link):
    global logo_found
    global logo_didnt_found
    driver.get(link)
    #Click "edit Page"
    sleep(5)
    wait = WebDriverWait(driver,15)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'btn btn-warning openPageInEditor')])[1]")))
    driver.execute_script("arguments[0].click()",next_button)

    sleep(8)

    try:
        #white logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')]")
        logo.click()
        #click on advance settings
        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings.click()
        #image input field
        sleep(5)
        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
        sleep(1)
        img_input.clear()
        sleep(1)
        img_input.send_keys('https://images.clickfunnels.com/77/ed40866d314783bde08dd7c5fbee1e/logowithshadow-150px.png')
        #close settings and Save

        go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
        # driver.execute_script("arguments[0],click()",go_back)
        # ActionChains(driver).move_by_offset(-70,20).click().perform()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
        save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
        sleep(1)
        driver.execute_script("arguments[0].click()",save__)
        sleep(5)

        logo_found += 1

    except:
        try:
            #black logo
            logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/8a/39d718264b4782bd5712737494a73b/ConfiLogoBLACK.png')]")
            logo.click()
            #click on advance settings
            advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
            advance_settings.click()
            #image input field
            sleep(5)
            img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
            sleep(1)
            img_input.clear()
            sleep(1)
            img_input.send_keys('https://images.clickfunnels.com/65/26fe99798a480486a41c6f71a13f95/LOGO-w-shadow-w-Black-Slogan-ss.png')
            #close settings and Save

            go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
            # driver.execute_script("arguments[0],click()",go_back)
            # ActionChains(driver).move_by_offset(-70,20).click().perform()
            sleep(1)
            # driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
            save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
            sleep(1)
            driver.execute_script("arguments[0].click()",save__)
            sleep(5)

            logo_found += 1

        except:
            logo_didnt_found += 1

        logo_didnt_found += 1






def collect_all_link():
    global link_list
    ###collect from link from side bar 
    link_funnel_step = driver.find_elements_by_xpath("//div[contains(@class,'funnel_step')]/div/a")
    for every_funnel_step_link in link_funnel_step:
        new_link = every_funnel_step_link.get_attribute("href")
        link_list.append(new_link)
        print(new_link)

    #collect link from dropdown 
    dropdown_link = driver.find_elements_by_xpath('//*[@id="other_steps"]/option')
    for every_dropdown_link in dropdown_link:
        new_links = every_dropdown_link.get_attribute("value")
        final_link = 'https://infoa9bf3f-app.clickfunnels.com'+str(new_links)
        link_list.append(final_link)
        print(final_link)

def main():
    global total
    # get_cookies()
    login_with_cookies()
    # collect_all_link()
    
    f = open('data3.json')
    links = json.load(f)

    
    # try:
    #     link_list.remove('https://infoa9bf3f-app.clickfunnels.com')
    # except:
    #     sleep(1)


    # with open('data.json','w') as f:
    #     json.dump(link_list,f)



    for page_link in links:
        print(page_link)
        print('data3')
        total += 1
        print('_____________________________________________')
        print('Pages check done =======>  '+ str(total))

        print('SEO added =====> '+str(seo_found)+ '\n' +'SEO not found  =====> '+str(seo_not_found) + '\n'+ 'footer added =====> '+str(footer_found)+'\n'+ 'Foodter didn\'t found  =====> '+ str(footer_didnt_found))



#start here
main()



