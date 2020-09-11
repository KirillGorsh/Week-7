# Google search scenario
# 1. Open the browser, launch the website google.com (Given condition in Gherkin scenario)
# 2. type 'selenium python' in the search and hit Enter (Actions - When)
# 3. Verify the result is more 20 mln (Test here, check point - Then)
# 4. Verify that it take less than second for search (Test here, check point - Then)
# 5. Close the browser

# keywords: HTML, locator: xpath, id, cssSelector, name, link_name, partial_link_name

####### <input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d"
# aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off"
# role="combobox" spellcheck="false" title="Search" value="python selenium" aria-label="Search"
# data-ved="0ahUKEwjyn-2c7tTrAhVyw1kKHdw3Ci8Q39UDCAo" xpath="1">

# input - element with 'tag' input
# attributes - describe the element to the browser to display on the GUI, selenium can use this to find elements

# CSS selector: (# means ID, . (dot) means class, )
# #tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input

# Xpath:
# chrome: //*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input
# chropath: //div[@class='a4bIc']//input[@name='q']

# copying whole element: <div id="result-stats" style="" xpath="1">About 25,300,000 results<nobr> (0.47 seconds)&nbsp;</nobr></div>






import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  #
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
driver.get("https://google.com")
print("opened the browser and google website")
time.sleep(3)

search_text_box = driver.find_element_by_name("q") # finding (locating) search box element in the HTML DOM
print("identified google search box")
time.sleep(3)

search_text_box.clear() # just in case clearing the search field
search_text_box.send_keys("python selenium") # enter provided taxt in the search box
print("cleared the search box then typed 'python selenium' words in it")
time.sleep(3)


search_text_box.send_keys(Keys.RETURN) # simulates hitting the ENTER key on your keyboard
print("hit the enter button")
time.sleep(3)

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)
result_msg_list = result_msg.split()
result_num_str = result_msg_list[1].replace(',', '')
result_num = int(result_num_str)
assert result_num > 20000000
print("Verifying result nuber Passed")

result_time_str = result_msg_list[3].replace('(', '')
result_time = float(result_time_str)
assert result_time < 1, "Search took more than a second!"
print("Verifying search performance Passed.")

print("now closing the browser...")
driver.close()
















