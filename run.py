from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import argparse
import json

# Set up the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--desktop", help="Make the tests only run desktop tests", action="store_true")
parser.add_argument("--mobile", help="Make the tests only run mobile tests", action="store_true")
parser.add_argument("--capabilities", help="Example: \
    \"{'browser': 'IE', 'browser_version': '8.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}\"")
args = parser.parse_args()

# Grab the authentication variables from the environment
try:
    selenium_username = os.environ['SELENIUM_AUTOMATE_USERNAME']
    selenium_value = os.environ['SELENIUM_AUTOMATE_VALUE']
except KeyError:
    print "You need to set the environment variables for your username and value. See the README.md for details"
    exit()

# If the user passed --capabilities "{...}" then that will be the only platform tested on
if(args.capabilities is not None):
    desired_cap_list = [json.loads(args.capabilities)]
# If the user did not pass the --capabilities argumen then run all the tests listed below
else:
    # This has been set as an array so that we can set multiple environments and run the tests below in a for loop
    # to repeat the tests for different operating systems. I have set a mobile capability list and
    # desktop capability list to allow the use of either or with a flag. More tests can easily be added. See the
    # browser stack website to get more options.
    # The below tests IE8, IE9, IE10 and IE11 on windows and then chrome, safari and Firefox on a Mac. Pay attention to
    # the version numbers.
    desktop_cap_list = [
        {'browser': 'IE', 'browser_version': '8.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'},
        {'browser': 'IE', 'browser_version': '9.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'},
        {'browser': 'IE', 'browser_version': '10.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'},
        {'browser': 'IE', 'browser_version': '11.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'},
        {'browser': 'Chrome', 'browser_version': '39.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1024x768'},
        {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1024x768'},
        {'browser': 'Safari', 'browser_version': '8.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1024x768'},
    ]

    # The below tests an iPhone 5 and Samsung Galaxy S5.
    mobile_cap_list = [
        {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'},
        {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S5'},
    ]

    # Conditionally create the desired_cap_list list. Didn't use elseif statements to allow for more user error
    desired_cap_list = []
    if(args.desktop is not None):
        # If the desktop argument has been passed, then only run the desktop tests
        desired_cap_list = desired_cap_list + desktop_cap_list
    if(args.mobile is not None):
        # If the mobile argument has been passed, then only run the mobile tests
        desired_cap_list = desired_cap_list + mobile_cap_list
    if(desired_cap_list == []):
        # If no desktop or mobile argument has been passed, then run both the desktop and mobile tests
        desired_cap_list = desktop_cap_list + mobile_cap_list

# This will run the the same test code in multiple environments
for desired_cap in desired_cap_list:
    # Output a line to show what enivornment is now being tested
    print "\nStarting Tests on %s %s on %s %s with a screen resolution of %s " % (desired_cap["browser"],
        desired_cap["browser_version"], desired_cap["os"], desired_cap["os_version"], desired_cap["resolution"])
    print "--------------------------------------------------\n"
    # Your test code should start here. This should really just be calling test functions in test classes
    # you set up though, for the sake of modularity
    driver = webdriver.Remote(
        command_executor="http://%s:%s@hub.browserstack.com:80/wd/hub" % (selenium_username, selenium_value),
        desired_capabilities=desired_cap)

    driver.get("http://www.google.com")
    if "Google" not in driver.title:
        raise Exception("Unable to load google page!")
    elem = driver.find_element_by_name("q")
    elem.send_keys("BrowerStack")
    elem.submit()
    print driver.title
    driver.quit()
