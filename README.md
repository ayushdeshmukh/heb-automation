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
* ShoppingList.txt
* HebMethod.py
* HebScan.py
