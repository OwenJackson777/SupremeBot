from selenium import webdriver
from config import information
from time import sleep

chrome = webdriver.Chrome('./chromedriver')

#Searching for link
while True:
    sleep(1.0)
    try:
        chrome.get(information['product_url'])
    except:
        print("Link not found.")
    else:
        break
print("Link Found")

def addToCart():
    chrome.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click() #add to cart
    chrome.implicitly_wait(1)
    chrome.find_element_by_xpath('//*[@id="cart"]/a[2]').click() #checkout

def fillOutFeilds(info):
    chrome.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(info['billing_name']) #name
    chrome.find_element_by_xpath('//*[@id="order_email"]').send_keys(info['email']) #email
    chrome.find_element_by_xpath('//*[@id="order_tel"]').send_keys(info['telephone']) #telephone
    chrome.find_element_by_xpath('//*[@id="bo"]').send_keys(info['address']) #address
    chrome.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(info['postal_code']) #postal code
    chrome.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(info['city']) #city
    chrome.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(info['creditcard_number']) #creditcard number
    chrome.find_element_by_xpath('//*[@id="orcer"]').send_keys(info['cvv']) #creditcard cvv

def selectCanada():
    chrome.find_element_by_xpath('//*[@id="order_billing_country"]/option[2]').click()

def selectDropDowns(info):
    provinces = ['', '', 'AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
    exp_month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    exp_year = [0, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031]

    province_index = provinces.index(info['province'])
    exp_month_index = exp_month.index(info['exp_month'])
    exp_year_index = exp_year.index(info['exp_year'])

    chrome.find_element_by_xpath(f'//*[@id="order_billing_state"]/option[{province_index}]').click() #province selection
    chrome.find_element_by_xpath(f'//*[@id="credit_card_month"]/option[{exp_month_index}]').click() #card expiration month
    chrome.find_element_by_xpath(f'//*[@id="credit_card_year"]/option[{exp_year_index}]').click() #card expiration year

def acceptTerms():
    chrome.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()

def placeOrder():
    chrome.find_element_by_xpath('//*[@id="pay"]/input').click()

if __name__ == "__main__":
    addToCart()
    fillOutFeilds(information)
    selectCanada()
    selectDropDowns(information)
    acceptTerms()
    #placeOrder()