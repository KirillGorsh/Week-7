from webdriver_class.webdriver_functions import *


email_input = "//input[@placeholder='Email or Phone']"
password_input = "//input[@placeholder='Password']"
login_button = ""

launch_website("https://www.facebook.com/marketplace/")
enter_text_by_xpath(email_input, "")
enter_text_by_xpath(password_input, "")
click_element_by_xpath(login_button)