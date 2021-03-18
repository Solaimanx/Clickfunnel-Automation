from selenium import webdriver
from time import sleep
import pickle
from selenium.webdriver.common.action_chains import ActionChains


# define the web driver
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')
driver.implicitly_wait(10)

#login 
def login_with_cookies():
    driver.get('https://app.clickfunnels.com/users/sign_in')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    print('login successfully')

def go_to_editor_and_change_img():
    driver.find_element_by_xpath("(//a[contains(@class,'btn btn-warning openPageInEditor')])[1]").click()
    sleep(5)
    if(driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/94/7774b1d84a44ea840f760845e5866f/FinalLogoWhite_600px_2021.png')]")):
        #black logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/94/7774b1d84a44ea840f760845e5866f/FinalLogoWhite_600px_2021.png')]")
        logo.click()
        image_settings = driver.execute_script("arguments[0].click();", logo)
        #image input field
        img_input = driver.find_elements_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div/input')[1]
        img_input.clear()
        img_input.send_keys('black new logo link')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
        print('black logo')
    
    elif(driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/94/7774b1d84a44ea840f760845e5866f/FinalLogoWhite_600px_2021.png')]")):
        #white logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/94/7774b1d84a44ea840f760845e5866f/FinalLogoWhite_600px_2021.png')]")
        logo.click()
        image_settings = driver.execute_script("arguments[0].click();", logo)
        #image input field
        img_input = driver.find_elements_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div/input')[1]
        img_input.clear()
        img_input.send_keys('white new logo link')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
        print('white logo')
    else:
        print('didn\'t found the logo')
        


def footer_remove_and_add():
    try:
        #try to find the footer text
        footer = driver.find_element_by_xpath("//div[contains(text(),'כל הזכויות שמורות ללדבר אנגלית ב 21 יום')]")
        hover = ActionChains(driver).move_to_element(footer)
        hover.perform()
        #hoverover on to show the settings
        move_little_up = ActionChains(driver).move_by_offset(50,20)
        move_little_up.perform()
        #click on remove and accept alert
        remove_section = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools-section')][not(contains(@style,'display: none'))][contains(@style,'opacity: 1')]/div/div[contains(@class,'de-rollover-remove-section')]")
        remove_section.click()
        alert = driver.switch_to.alert
        alert.accept()
    except:
        print('Dont have footer')


def drag_and_drop():
    section = driver.find_element_by_xpath("//div[contains(@class,'editorTopNavItemX editorTopNavItemShowSub pull-left')]/span[contains(text(),'Sections')]")
    hover_section = ActionChains(driver).move_to_element(section)
    hover_section.perform()
    add_section = driver.find_element_by_xpath("/html/body/div[68]/div[2]/div[1]/div[1]/div/div[1]")
    add_section.click()
    sleep(2)
    
    driver.find_element_by_xpath('//*[@id="personalSections"]').click()
    sleep(2)
    # drag and drop source and targets elements
    drag = driver.find_element_by_xpath('//*[@id="personal_section_templates"]/div[37]')
    drop = driver.find_elements_by_xpath("//div[contains(@class,'dropZoneForSections ui-droppable')]")[-1]
    drog__drop = ActionChains(driver).click_and_hold(drag).pause(4).move_by_offset(-30,10).move_to_element(drop).release(drop)
    drog__drop.perform()
    #save
    driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()


def seo_meta_tag():
    settings = driver.find_element_by_xpath('//*[@id="editorTopNav_settings"]')
    hover_settings = ActionChains(driver).move_to_element(settings)
    hover_settings.perform()
    #click on settings > Seo meta data
    add_seo_meta_tag = driver.find_element_by_xpath('//*[@id="editorTopNav_settings"]/div/div[2]')
    add_seo_meta_tag.click()
    sleep(2)
    #meta data
    seo_meta_data = driver.find_elements_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div/input')[1]
    seo_meta_data.clear()
    seo_meta_data.send_keys('seo meta tag')
    #description
    seo_description = driver.find_elements_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div/input')[2]
    seo_description.clear()
    seo_description.send_keys('seo description')
    #keywards
    seo_keywards = driver.find_elements_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div/input')[3]
    seo_keywards.clear()
    seo_keywards.send_keys('seo keywards')
    #close settings and Save
    driver.find_element_by_xpath('/html/body/div[11]').click()
    driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()



def main():
    login_with_cookies()
    go_to_editor_and_change_img()
    # footer_remove_and_add()
    # drag_and_drop()


#start here
main()
