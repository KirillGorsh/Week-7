from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys

from webdriver_class.webdriver_functions import *


sign_in_link = "//a[@class='login']"
email_create = "//input[@id='email_create']"
button_create = "//button[@id='SubmitCreate']"
gender_input = "//input[@id='id_gender1']"
gender_text = "//div[@class='clearfix']//div[1]//label[1]"
first_name_input = "//input[@id='customer_firstname']"
last_name_input = "//input[@id='customer_lastname']"
password_input = "//input[@id='passwd']"
firstname_input = "//input[@id='firstname']"
lastname_input = "//input[@id='lastname']"
address_input = "//input[@id='address1']"
city_input = "//input[@id='city']"
state_select = "//select[@id='id_state']"
zip_input = "//input[@id='postcode']"
country_select = "//select[@id='id_country']"
mobile_phone_input = "//input[@id='phone_mobile']"
register_button = "//button[@id='submitAccount']"
actions = ActionChains(driver)


launch_website("http://automationpractice.com/index.php")
click_element_by_xpath(sign_in_link)
time.sleep(2)
enter_text_by_xpath(email_create, "kirill1111@mail.com")
click_element_by_xpath(button_create)
time.sleep(2)
click_element_by_xpath(gender_input)
print(f"\tGender selected: ")
time.sleep(1)
enter_text_by_xpath(first_name_input, "Kirill")
print("\tFirst name entering")
time.sleep(1)
enter_text_by_xpath(last_name_input, "Gor")
print("\tLast name entering")
time.sleep(1)
enter_text_by_xpath(password_input, "qwerty12345")
if len(password_input):
    len(password_input)
    print("\tPassword created")
else:
    print("\tPassword must content at least 5 characters")
time.sleep(1)
# enter_text_by_xpath(firstname_input, "Kirill")
# enter_text_by_xpath(lastname_input, "Gor")
enter_text_by_xpath(address_input, "22 Wall street")
print("\tAddress entering")
time.sleep(1)
enter_text_by_xpath(city_input, "New York")
print("\tCity entering")
time.sleep(1)
click_element_by_xpath(state_select)
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ENTER).perform()
print("\tState selected")
time.sleep(1)
enter_text_by_xpath(zip_input, "10002")
print("\tZipCode entering")
time.sleep(1)
click_element_by_xpath(country_select)
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ENTER).perform()
print("\tCountry selected")
time.sleep(1)
enter_text_by_xpath(mobile_phone_input, "2433425566")
print("\tMobile phone number entering")
time.sleep(1)
click_element_by_xpath(register_button)
print("\tRegistration passed")






