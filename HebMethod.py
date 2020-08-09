from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
from selenium.common.exceptions import NoSuchElementException


#PRECONDITION: user has an account, wants to re-order using the account, find a delivery slot


shoppingListDeck = []
files = open("ShoppingList.txt", "r")
lists = files.readlines()
for i in range (len(lists)):
    shoppingListDeck.append(lists[i].strip('\n'))
#print (shoppingListDeck)

    
      

driver = webdriver.Chrome(executable_path=r"C:\Users\Ayush\Python\chromedriver.exe") #open url
driver.get("https://www.heb.com")
    
driver.implicitly_wait(3000)
    
logInXpath = '/html/body/div[2]/div/div/div[2]/div/header/nav[1]/ul/li[1]/a[1]'
logInBox = driver.find_element_by_xpath(logInXpath)
logInBox.click()
    
driver.implicitly_wait(3000)

emailXpath = '/html/body/div[1]/div[3]/div[1]/div[1]/form/div[3]/div[1]/input[1]' #enter email
emailBox = driver.find_element_by_xpath(emailXpath) 
emailBox.send_keys("bobjonespythontest@gmail.com") 
    
driver.implicitly_wait(3000)
    
pwXpath = '/html/body/div[1]/div[3]/div[1]/div[1]/form/div[3]/div[1]/input[3]' #enter password and login
pwBox = driver.find_element_by_xpath(pwXpath) 
pwBox.send_keys("pythont3st")

driver.implicitly_wait(3000)

pwBox.send_keys(Keys.ENTER)

def HEB(list):
    
    for x in list:
         
        driver.implicitly_wait(3000)
                
        searchXpath = '//*[@id="searchText"]'
        searchBox = driver.find_element_by_xpath(searchXpath)
        searchBox.click()
        searchBox.send_keys(x)
        searchBox.send_keys(Keys.ENTER)
    
        driver.implicitly_wait(3000)
            
        cartTagName = 'div.add-to-cart-button-container'
        cartBox = driver.find_element_by_tag_name(cartTagName)
        cartBox.click()
        
        driver.implicitly_wait(3000)
        
        """
            driver.switch_to.active_element
            
            driver.implicitly_wait(3000)
            
            okXpath = '//*[@id="representative-product-modal___BV_modal_footer_"]/button'
            okBox = driver.find_element_by_xpath(okXpath)
            okBox.click()
        """
        
        
        driver.implicitly_wait(3000)
            
        searchClearXpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[2]/form/button[2]/img'
        searchClearBox = driver.find_element_by_xpath(searchClearXpath)
        searchClearBox.click()
            
        
HEB(shoppingListDeck)



