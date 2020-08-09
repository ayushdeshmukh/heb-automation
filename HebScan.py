from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import Client


#PRECONDITION: User has account and set address, with settings set to delivery and NOT curbside.

def sendMessage(pickerString):
    account_sid = 'AC64f312bd660ab165255edb29228d3796' # Found on Twilio Console Dashboard
    auth_token = 'aea7a379565b0e70476a3d5dc9a53398' # Found on Twilio Console Dashboard
    
    myPhone = '+15127360151' # Phone number you used to verify your Twilio account
    TwilioNumber = '+12055128568' # Phone number given to you by Twilio
    
    client = Client(account_sid, auth_token)
    
    client.messages.create(to=myPhone,from_=TwilioNumber,body=pickerString)
 

 

def login(): #logs into HEB.com from the login page
    
    driver.implicitly_wait(3000)
    
    emailXpath = '/html/body/div[1]/div[3]/div[1]/div[1]/form/div[3]/div[1]/input[1]' #enter email
    emailBox = driver.find_element_by_xpath(emailXpath) 
    emailBox.send_keys("bobjonespythontest@gmail.com") 
    
    driver.implicitly_wait(3000)
    
    pwXpath = '/html/body/div[1]/div[3]/div[1]/div[1]/form/div[3]/div[1]/input[3]' #enter password and login
    pwBox = driver.find_element_by_xpath(pwXpath) 
    pwBox.send_keys("pythont3st")
    pwBox.send_keys(Keys.ENTER)
    
    driver.implicitly_wait(3000)
    

def accessTimeSlots(): # clicks on the box to trigger the timeslot popup for pickups/curbside
    
    driver.implicitly_wait(3000)
    
    timeSlotSelector = '#js-sticky-search > div.site-header__reservation-display > div > bootstrap > div > button'
    timeSlotBox = driver.find_element_by_css_selector(timeSlotSelector)
    timeSlotBox.click()
    
    driver.implicitly_wait(3000)
  
def checkPicker(): #checks green status bar on the bottom to see if slot is reserved, and the details of the delivery
    pickerXpath = "/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]"
    pickerBox = driver.find_element_by_xpath(pickerXpath)
    pickerString = pickerBox.text
    return pickerString

def checkDays(): #checks all days for open slots, appends their label ("full" or something else) to a list
    dayString = []
        
    driver.implicitly_wait(3000) 
        
        
    day1Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[1]/div[2]'
    day1Box = driver.find_element_by_xpath(day1Xpath)
    day1String = day1Box.text
    dayString.append(day1String)
    #print(day1String)
        
        
    driver.implicitly_wait(3000) 
    
    day2Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[2]/div[2]'
    day2Box = driver.find_element_by_xpath(day2Xpath)
    day2String = day2Box.text
    dayString.append(day2String)
    #print(day2String)
    
    driver.implicitly_wait(3000) 
    
    day3Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[3]/div[2]'
    day3Box = driver.find_element_by_xpath(day3Xpath)
    day3String = day3Box.text
    dayString.append(day3String)
    #print(day3String)
    
    driver.implicitly_wait(3000) 
    
    day4Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[4]/div[2]'
    day4Box = driver.find_element_by_xpath(day4Xpath)
    day4String = day4Box.text
    dayString.append(day4String)
    #print(day4String)
    
    driver.implicitly_wait(3000) 
    
    day5Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[5]/div[2]'
    day5Box = driver.find_element_by_xpath(day5Xpath)
    day5String = day5Box.text
    dayString.append(day5String)
    #print(day5String)
    
    driver.implicitly_wait(3000) 
    
    nextXpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/button[1]'
    nextBox = driver.find_element_by_xpath(nextXpath)
    nextBox.click()
    
    driver.implicitly_wait(3000) 
    
    day6Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[3]/div[2]'
    day6Box = driver.find_element_by_xpath(day6Xpath)
    day6String = day6Box.text
    dayString.append(day6String)
    #print(day6String)
    
    driver.implicitly_wait(3000) 
    
    day7Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[4]/div[2]'
    day7Box = driver.find_element_by_xpath(day7Xpath)
    day7String = day7Box.text
    dayString.append(day7String)
    #print(day7String)
    
    driver.implicitly_wait(3000) 
    
    day8Xpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/section[1]/div/div/button[5]/div[2]'
    day8Box = driver.find_element_by_xpath(day8Xpath)
    day8String = day8Box.text
    dayString.append(day8String)
    #print(day8String)
    
    driver.implicitly_wait(3000) 
    
    return(dayString)
    
def reserveSlot(): #clicks reseve button to reserve a slot
    deliveryXpath = '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]'
    deliveryBox = driver.find_element_by_xpath(deliveryXpath)
    deliveryBox.click()
               
    driver.implicitly_wait(3000)
        

def checkTimeSlot(): #reads the daystring list to check for open days, clicks reserve if open, and returns slot reserved if already there
    
    
    driver.implicitly_wait(3000)  
    
    driver.switch_to.active_element
    
    driver.implicitly_wait(3000) 
    
    pickerString = checkPicker()
    
    driver.implicitly_wait(3000) 
    
    dayString = checkDays()
    
    driver.implicitly_wait(3000) 

    if pickerString == "":
        
        for i in range(len(dayString)):
            if dayString[i] != "Full":
                reserveSlot()
                break
    else:
        time.sleep(5) 
        
        print("Slot reserved - "+pickerString) 
        sendMessage("Slot reserved - "+pickerString)
        time.sleep(3600)

def tearDown(): #shuts down chromedriver
    driver.quit()



for i in range(3):
    driver = webdriver.Chrome(executable_path=r"C:\Users\Ayush\Python\chromedriver.exe")
    driver.get("https://www.heb.com/my-account/login")
    login()
    accessTimeSlots()
    checkTimeSlot()
    
    time.sleep(5)
    
    tearDown()



