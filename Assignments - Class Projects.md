# Class Assignments

## Project 1: Creating an account in automationpractice.com

- Sign In> enter email> click on Create Account > Fill the forms
- finding all elements (xpath, id, name)
- verify that account is created by message, logout button

Example to verify a text after creating the account.

```python
from selenium import webdriver
driver = webdriver.Chrome()

heading_xpath = "//h1[@class='page-heading']"
element = driver.find_element_by_xpath(heading_xpath)
assert 'Your Account' in element.text

```

## Project 2 (hard project): Creating facebook marketplace list with uploading a file
### Precondition: You need to save your username and password in the yml data file.
- Name your file as config.yml
- Add your file name into .gitignore. Dont Add to Git if pyCharm prompts you when you create a file.

```gitignore
.idea/
data/config.yml
```
- use this functions to read from yaml file.
```python
# you need to install yaml before importing
# pip install pyyaml or yaml
import yaml
from os.path import dirname, abspath

ROOT_DIR = dirname(dirname(abspath(__file__)))
def load_yaml(filepath):
    with open(filepath, 'r') as data:
        document = yaml.safe_load(data)
    return document
```

```yaml
# data/config.yml
url: "http://automationpractice.com/index.php"
email: "hello@email.com"
password: "$Password001"
```

to use the email and password in your test on your file with test steps load the data first using following lines: 
```python
# import the file where you functions are saved.
from steps.webelement_functions import *

data = load_yaml(f"{ROOT_DIR}/data/config.yml")

url = data['url']
email = data['email']
password = data['password']
```

To read more about yml file [here](https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/)

### Scenario 1
- open browser, launch the "https://www.facebook.com/marketplace",
- login to facebook

### Scenario 2
- create new listing, choose item for sale, verify the url: "https://www.facebook.com/marketplace/create/item"

Here is the some of the locators you will need:

```python
# imports here

upload_xpath = "//input[@type='file' and contains(@accept, 'image')]"
price_input = "//label[@aria-label='Price']//input[contains(@id, 'jsc_c_')]"
title_input = "//label[@aria-label='Title']//input[contains(@id, 'jsc_c_')]"
category_list = "//label[@aria-label='Category']//span"
category_item = "//span[contains(text(),'Electronics')]"
category_sub_item = "//span[contains(text(),'Blank Media')]"
condition_list = "//span[contains(text(),'Condition')]"
condition_option = "//div[contains(text(),'Used - Like New')]"
next_button_xpath = "//div[@aria-label='Next']"
title = 'Iphone25'

# image_path = "C:\\Users\\akhus\Desktop\\thinkorswim-simulated-trading.png"
image_path = "C:/Users/akhus/Desktop/thinkorswim-simulated-trading.png"
image_upload = driver.find_element_by_xpath(upload_xpath)
image_upload.send_keys(image_path)

# to check next button is enabled:
next_button = driver.find_element_by_xpath(next_button_xpath)
if next_button.is_enabled():
    next_button.click()
    print("Next button is clicked.")
```

- after listing is published verify url= "https://www.facebook.com/marketplace/you/selling"
- verify the item is listed

```python
active_item1_xpath = f"//span[contains(text(), '{title}')]"
active_item1 = driver.find_element_by_xpath(active_item1_xpath)
time.sleep(5)
assert active_item1.is_displayed()
print("Test is successfully executed!!")
```

### Scenario 3

Remove the item from the list.

```python
# last line should be 
assert not active_item1.is_displayed()
```


## How to Submit
- Commit, push to your github
- Submit your github links in this [google form.](https://forms.gle/doeKiU6CkNdc4jm28)

