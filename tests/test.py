import time
from random import randint
from selenium import webdriver

# initialize random number for the Email
RandomNumber = randint(25, 250000)
StrRanNUm = str(RandomNumber)

# Deposit & Card details
Amount = "1.15"
NameOnCard = "Bnology Limited"
CardNumber = "5357090007007585"
Expiration = "0724"
CVVNumber = "397"

# Registration details
FullName = "test"
Email = StrRanNUm + "@testbnology.com"
Password = "Aa1122"
PhoneCountryCode = "972"
PhoneNumber = "559793138"


# initialize web page
web = webdriver.Chrome(executable_path='C:/Users/Maor.Hassan.bn/Desktop/chromedriver_win32/chromedriver.exe')
web.get('https://trader.alvexo.eu/login-area-new/sign-up')

time.sleep(1)



# Page 1
# Sign up fill page
name = web.find_element_by_xpath('//*[@id="sign_up_form"]/div[2]/div/div[1]/input')
name.send_keys(FullName)

mail = web.find_element_by_xpath('//*[@id="sign_up_form"]/div[3]/div/div[1]/input')
mail.send_keys(Email)

password = web.find_element_by_xpath('//*[@id="sign_up_form"]/div[4]/div/div[1]/input')
password.send_keys(Password)

agreeRadioButton = web.find_element_by_xpath('//*[@id="sign_up_form"]/div[5]/div/input')
agreeRadioButton.click()

continueButton = web.find_element_by_xpath('//*[@id="sign_up_form"]/button')
continueButton.click()

time.sleep(2.5)

# Page 2
# Phone fill page
countryCode = web.find_element_by_xpath('//*[@id="phone_form"]/div[3]/div[1]/div[1]/input')
countryCode.clear()
countryCode.send_keys(PhoneCountryCode)

phone = web.find_element_by_xpath('//*[@id="phone_form"]/div[3]/div[1]/div[2]/input')
phone.send_keys(PhoneNumber)

signUpButton = web.find_element_by_xpath('//*[@id="phone_form"]/button')
signUpButton.click()

time.sleep(7)

depositButton = web.find_element_by_xpath('//*[@id="app"]/section[1]/div/div[3]/button')
time.sleep(8)
depositButton.click()
time.sleep(8)

# Click on 'deposit founds' button
depositFoundsButton = web.find_element_by_xpath('// *[ @ id = "app"] / header / div[3] / div[1]')
depositFoundsButton.click()

# Page 3
# Amount fill page
amount = web.find_element_by_xpath('//*[@id="visa"]/form/div/div[1]/input')
time.sleep(2)
amount.clear()
time.sleep(1)
amount.send_keys(Amount)

nextButton = web.find_element_by_xpath('//*[@id="visa"]/form/div/div[4]')
nextButton.click()

time.sleep(2)

# Page 4
# Credit card fill page
nameOfCard = web.find_element_by_xpath('//*[@id="visa"]/form/div/div[2]/input')
nameOfCard.send_keys(NameOnCard)

cardNumber = web.find_element_by_xpath('//*[@id="ccn"]')
cardNumber.send_keys(CardNumber)

expiration = web.find_element_by_xpath('//*[@id="expDate"]')
expiration.send_keys(Expiration)

cvv = web.find_element_by_xpath('//*[@id="visa"]/form/div/div[4]/div[2]/div/input')
cvv.send_keys(CVVNumber)

depositAmount = web.find_element_by_xpath('// *[ @ id = "visa"] / form / div / button')
depositAmount.click()
time.sleep(20)

code = web.find_element_by_xpath('//*[@id="Credential_Value"]')
code.send_keys(11)











