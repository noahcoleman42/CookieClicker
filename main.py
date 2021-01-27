# Written by Noah Coleman
# 11/12/2020

# This is an intro to "Action Chains"
# This program will play cookie clicker and perform automatic upgrades.
# We can store a list of actions in a queue, and perform them in a sequence

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\\Program Files (x86)\\Mine\\Apps\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# When we get to the page, the elements won't be there right away, so we have to wait for the page to load.
# This is called an implicit wait
driver.implicitly_wait(5)

# Cookie to click and cookie count elements
cookie = driver.find_element_by_id("bigCookie")
numberOfCookies = driver.find_element_by_id("cookies")

# List of upgrade elements
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]       #(start, stop, step)

# Creating an action chain object called actions using our driver
actions = ActionChains(driver)

# The first thing to add to the action chain is clicking the cookie constantly
actions.click(cookie)
actions.perform()

for i in range(5000):
    # perform all the actions we described above (click)
    actions.perform()
    # take the first value before the split in numberOfCookies.text, and convert it to an integer.
    count = int(numberOfCookies.text.split(" ")[0].replace(" , " , ""))
    # for each item in the upgrades section, check if we can afford the upgrade from "best" to "worst"
    # if we can, move cursor to the upgrade, and click.
    for item in items:
        cost = int(item.text)
        if cost <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.double_click()
            upgrade_actions.perform()
