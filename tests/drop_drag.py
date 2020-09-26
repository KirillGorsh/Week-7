import time

from selenium.webdriver import ActionChains

from webdriver_class.webdriver_functions import launch_website, driver, close_browser

# item1_xpath = "//div[@id='draggable']//p[contains(text(),'Drag me to my target')]"
# # item2_xpath = "//div[@id='todrag']//span[contains(text(),'Draggable 2')]"
# drop_zone_xpath = "//div[@id='droppable']"
# dropped_item1 = "//div[@id='draggable']"
# # dropped_item2 = "//div[@id='droppedlist']//span[contains(text(),'Draggable 2')]"
#
# launch_website("http://testautomationpractice.blogspot.com/")
# item1 = driver.find_element_by_xpath(item1_xpath)
# drop_zone = driver.find_element_by_xpath(drop_zone_xpath)
#
# actions = ActionChains(driver)
# actions.drag_and_drop(item1,drop_zone).pause(2).perform()
# print('Dropped')
# close_browser()


launch_website("https://letskodeit.teachable.com/p/practice")

xpath1 = "//div[@id='radio-btn-example']"
radio_button_example = driver.find_element_by_xpath(xpath1)
print(f"radio button example is displayed: ", {radio_button_example.is_displayed()})

if radio_button_example.is_displayed():
    bmw_option = driver.find_element_by_xpath("//input[@id='bmwradio']")
    bmw_option.click()
    time.sleep(2)
else:
    print("radio button example is not displayed")

print("test passed")
button = driver.find_element_by_xpath("//button[@id='openwindow']")











