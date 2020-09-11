import time
from selenium import webdriver

# Initializing a new browser
driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://letskodeit.teachable.com/p/practice")
print("opened the browser and letskodeit website")
time.sleep(0)

# 1. Find all buttons
buttons = driver.find_elements_by_xpath('//button')
for button in buttons:
    print('text of button:', button.text)

# 2. Find by link text
open_tab = driver.find_element_by_link_text('Open Tab')
open_tab2 = driver.find_element_by_partial_link_text('en Tab')
# open_tab.click()
time.sleep(5)

# 3. using WebDriver class properties
url1 = driver.current_url
title1 = driver.title
win_handle1 = driver.current_window_handle
name1 = driver.name
print('Current url:', url1)
print('Current title1:', title1)
print('Current win_handle1:', win_handle1)
print('Current name1:', name1)

open_tab.click()

# switch to a new tab, WebDriver Method - switch_to.window(new_handle)
handles = driver.window_handles
print(handles)

url2 = ""
title2 = ""
win_handle2 = ""

for handle in handles:
    if handle != win_handle1:
        driver.switch_to.window(handle)

    url2 = driver.current_url
    title2 = driver.title
    win_handle2 = driver.current_window_handle

print('Current url2:', url2)
print('Current title2:', title2)
print('Current win_handle2:', win_handle2)
assert url2 == 'https://letskodeit.teachable.com/courses'
assert title2 == "Let's Kode It"


# 4. Close the tab and browser
driver.close()
print("close the current tab")
time.sleep(5)

#switch back to initial window handle
driver.switch_to.window(win_handle1)

print('current_url after closing a new tab:', driver.current_url)
print('current_window_handle after closing a new tab:', driver.current_window_handle)
driver.quit()
print("browser is closed")