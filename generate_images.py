import json
import time
import os

from pyvirtualdisplay import Display
from selenium import webdriver

data = json.load(open('project.json', 'r'))
url = data['url']
gecko_path = data['gecko_path']
selector = data['selector']
output_image_name = data['output_image_name']
output_image_folder = data['output_image_folder']


def get_file_screenshot(url):
    try:
        display = Display(visible=0, size=(1800, 1600))
        display.start()
        # now  Firefox will run in a virtual display.
        browser = webdriver.Firefox(executable_path=gecko_path)
        # browser.set_window_size(2046, 2046)
        # browser.fullscreen_window()
        browser.implicitly_wait(30)
        browser.set_page_load_timeout(150)
        browser.get(url)
        time.sleep(30)
        elements = browser.find_elements_by_css_selector(selector)
        i = 0
        if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/" + output_image_folder):
            os.makedirs(output_image_folder)
        for element in elements:
            i = i + 1
            element_png = element.screenshot_as_png
            with open(f"{output_image_folder}/{output_image_name}{i}.png", "wb") as file:
                file.write(element_png)
        # browser.get_screenshot_as_png(filename="test.png")
        browser.quit()
        display.stop()
    except Exception as e:
        print(e)


get_file_screenshot(url)
