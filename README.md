# heb-automation
Automate the searching, shopping, and order of grocery items through [HEB Grocery's](https://www.heb.com/ "HEB") website.

## Requirements
This project is run on Python 3.7 through [Anaconda's](https://www.anaconda.com/products/individual "Anaconda individual download site") Spyder 4 IDE. The precondition for this project is that the user already has an [HEB online account](https://www.heb.com/my-account/user-register "Resgister for an HEB online account") with an associated email address, password, and home delivery address on file with the store.

## Installation
The key file needed to run this project is a [Chromedriver](https://chromedriver.chromium.org/downloads "Chromedriver download site") file that automates your keystrokes and is compatible with your version of Chrome. Make sure you check the version of Chrome you're using by going to "Chrome Settings" and "About Chrome", then download the file that corresponds to it. Next, use [pip](https://pip.pypa.io/en/stable/installing/ "pip installation documentation") to install [Selenium](https://www.selenium.dev/ "SeleniumHQ Browser Automation") in the command prompt (use Anaconda's native command prompt from the Anaconda launcher if you're using Spyder like I did). 
```bash
pip install selenium
```
### [Twilio](https://www.twilio.com/messaging "Twilio Messaging API")
This project makes use of Twilio's Messaging API to send the user an automated message whenever a delivery spot on the HEB website opens up. Follow their [Python quickstart](https://www.twilio.com/docs/sms/quickstart/python "Twilio Messaging API: Python quickstart") guide to get your ***account SID***, ***authorization token***, and ***Twilio phone number***. From there, you're ready to get started!

## Usage
There are 3 other files in this repository:
* [ShoppingList.txt](ShoppingList.txt)
  * Shopping list full of items that the project reads, searches for, and adds to cart in the HEB website.
* [HebMethod.py](HebMethod.py)
  * The file that logs into your HEB account, reads the shopping list, and searches/adds the items to your cart.
* [HebScan.py](HebScan.py)
  * The file that constantly scans the HEB delivery schedule, and notifies you via text when there is an opening while blocking off that open spot.
### Shopping List
Open the ShoppingList.txt file, and input your shopping list items like "eggs, milk, bananas, etc.". Write each item on its own line, allowing the HebMethod.py file to read each item as a distinct string object and append it to a list.
#### ShoppingList.txt Example:
```
eggs
milk
bananas
```
#### Reading ShoppingList.txt in HebMethod.py
```python
shoppingListDeck = []
files = open("ShoppingList.txt", "r")
lists = files.readlines()
for i in range (len(lists)):
    shoppingListDeck.append(lists[i].strip('\n'))
```
### HEB Method
Open the HebMethod.py file. To run this file, you'll need to have your ShoppingList.txt file filled out and saved in the same directory as HebMethod.py. Once that's complete, there are only 3 variables in the file you'll need to update:
* The path to your Chromedriver file: ```chromeDriverPath = #enter the path for your chromedriver file```
* The email associated with your online HEB account: ```email = #enter the email of your HEB account```
* The password to the account: ```password = #enter your password for your HEB account```

Once you update finish your ShoppingList.txt and update the above variables, you're ready to run HebMethod.py!
### HEB Scan
For this file, you'll have to do the same updates to the ```chromeDriverPath```, ```email```, and ```password``` variables for your HEB account. However, it is this section of the project where you have to use the Twilio Messaging API integration that you performed earlier. Again, if you follow their Python quickstart tutorial, it should take you to an account dashboard where you'll find your ***account SID***, ***authorization token***, and ***Twilio phone number***. Using those values, update the corresponding variables in this section:
```python
def sendMessage(pickerString):
    account_sid = # Found on Twilio Console Dashboard
    auth_token =  # Found on Twilio Console Dashboard
    
    myPhone = # Phone number you used to verify your Twilio account
    TwilioNumber = # Phone number given to you by Twilio
    
    client = Client(account_sid, auth_token)
    
    client.messages.create(to=myPhone,from_=TwilioNumber,body=pickerString)
```    
The file will then scan for open delivery spots, and when it finds one, it will reserve the slot for you and send a message to your phone that looks something like this:
```
Sent from your Twilio trial account 
- Slot reserved - You're scheduled for May 03, 5:30PM-6:30PM.
Your time slot will be held until 11:18 PM
```
That's pretty much it!

## Troubleshooting
The success of the script is heavily predicated on Chromedriver's ability to locate the different elements on the page that you want to click on. For this I primarily used ***XPath locators***, which are found by inspecting the element of a button on a webpage. 

### Here's what it looks like on HEB.com:
![XPath-Example](https://user-images.githubusercontent.com/66505806/89741605-2e7ad300-da58-11ea-855e-866b290f44bf.png)
### And here's how the code executes it:
```python
logInXpath = '/html/body/div[2]/div/div/div[2]/div/header/nav[1]/ul/li[1]/a[1]'
logInBox = driver.find_element_by_xpath(logInXpath)
logInBox.click()
```
