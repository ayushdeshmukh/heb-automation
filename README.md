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
Open the HebMethod.py file. To run this file, you'll need to have your ShoppingList.txt file filled out, and be sure that it's saved in the same directory as HebMethod.py. Once that's complete, there are only 3 variables in the file you'll need to update:
* The path to your Chromedriver file: ```chromeDriverPath = #enter the path for your chromedriver file```
* The email associated with your online HEB account: ```email = #enter the email of your HEB account```
* The password to the account: ```
