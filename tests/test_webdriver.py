
from webdriver_class.webdriver_functions import *
from webdriver_class.webelement_functions import *

data = load_yaml(f"{ROOT_DIR}/data/config.yml")

web_url = data['scenario1']['web_url']
username = data['scenario1']['username']
password = data['scenario1']['password']
# login_to_automation_practice(web_url, username, password)


# test_right_click()
# test_drag_and_drop()
# test_radio_button_is_displayed_selected()
# test_det_attribute()
# test_drop_down_list()
# test_alerts()
test_mouse_hovering()