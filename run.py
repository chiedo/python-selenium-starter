from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import argparse
import ast

# Set up the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--desktop", help="Make the tests only run tests on desktop computers. Boolean.",
                    action="store_true")
parser.add_argument("--mobile", help="Make the tests only run tests on mobile devices. Boolean.", action="store_true")
parser.add_argument("--base_url", help="A way to override the DEFAULT_BASE_URL for your tests.",)
parser.add_argument("--test", help="Only run one test as specified", default="all")
parser.add_argument("--capabilities", help="Example: \"{'browser': 'IE', 'browser_version': '8.0', 'os': 'Windows', " +
                    "'os_version': '7', 'resolution': '1024x768'}\"")
args = parser.parse_args()

# SET UP YOUR STATIC VARIABLES BELOW
DEFAULT_BASE_URL = "http://www.google.com"  # Set this

if(args.base_url is not None):
    # Override the DEFAULT_BASE_URL value if passed in via the command line arg
    BASE_URL = args.base_url  # Don't touch this
else:
    BASE_URL = DEFAULT_BASE_URL


# Grab the authentication variables from the environment
try:
    selenium_username = os.environ['SELENIUM_AUTOMATE_USERNAME']
    selenium_value = os.environ['SELENIUM_AUTOMATE_VALUE']
except KeyError:
    print "You need to set the environment variables for your username and value. See the README.md for details"
    exit()


if(BASE_URL == ""):
    print "You need to set your DEFAULT_BASE_URL variable at the top of run.py."
    exit()

if(args.capabilities is not None):
    # If the user passed --capabilities "{...}" then that will be the only platform tested on

    # convert the string into a python dictionary so it can be used in as a desired capability
    desired_cap_list = [ast.literal_eval(args.capabilities)]
else:
    # If the user did not pass the --capabilities argumen then run all the tests listed below

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
        {'browser': 'Chrome', 'browser_version': '39.0', 'os': 'OS X', 'os_version': 'Yosemite',
         'resolution': '1024x768'},
        {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'OS X', 'os_version': 'Yosemite',
         'resolution': '1024x768'},
        {'browser': 'Safari', 'browser_version': '8.0', 'os': 'OS X', 'os_version': 'Yosemite',
         'resolution': '1024x768'},
    ]

    # The below tests an iPhone 5 and Samsung Galaxy S5. If your Selenium Automate plan doesn't include Mobile, you will
    # Want to change the following to mobile_cap_list = []
    mobile_cap_list = [
        {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'},
        {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S5'},
    ]

    # Conditionally create the desired_cap_list list. Didn't use elseif statements to allow for more user error
    desired_cap_list = []
    if(args.desktop):
        # If the desktop argument has been passed, then only run the desktop tests
        desired_cap_list = desired_cap_list + desktop_cap_list
    if(args.mobile):
        # If the mobile argument has been passed, then only run the mobile tests
        desired_cap_list = desired_cap_list + mobile_cap_list
    if(desired_cap_list == []):
        # If no desktop or mobile argument has been passed, then run both the desktop and mobile tests
        desired_cap_list = desktop_cap_list + mobile_cap_list

# This will run the the same test code in multiple environments
for desired_cap in desired_cap_list:
    # Output a line to show what enivornment is now being tested
    if("browser" in desired_cap):
        # For desktop
        print "\nStarting Tests on %s %s on %s %s with a screen resolution of %s " % (desired_cap["browser"],
            desired_cap["browser_version"], desired_cap["os"], desired_cap["os_version"], desired_cap["resolution"])
    else:
        # For mobile
        print "\nStarting Tests on a %s" % (desired_cap["device"])

    print "--------------------------------------------------\n"

    # YOUR TEST CODE SHOULD START HERE
    # This should really just be calling test functions in test classes
    # you set up though, for the sake of modularity
    driver = webdriver.Remote(
        command_executor="http://%s:%s@hub.browserstack.com:80/wd/hub" % (selenium_username, selenium_value),
        desired_capabilities=desired_cap)

    # Test One
    if(args.test is "all" or args.test == "example_a.py"):
        from tests.example_a import Test
        test = Test(driver, BASE_URL)
        test.run()

    # Test Two
    if(args.test is "all" or args.test == "example_b.py"):
        from tests.example_b import Test
        test = Test(driver, BASE_URL)
        test.run()

    # More and more tests can be added in this exact way

    # Clean Up
    driver.quit()
