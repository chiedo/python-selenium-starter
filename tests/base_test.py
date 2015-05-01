"""A test class for others to inherit to prevent duplicate code."""

from selenium.webdriver.support.ui import WebDriverWait
import time


class BaseTest(object):
    def __init__(self, driver, base_url, module):
        """Init

        Parameters
        ----------
        driver : object
            The selenium web driver
        base_url : string
            The base url of the web page we will be visiting.
        module
            The module currently being executed
        """
        self.driver = driver
        self.base_url = base_url
        self.module = module
        self.wait = WebDriverWait(driver, 10)

    def failed(self, error_message):
        """Print a generic message when a test has failed, take a screenshot and end the test.
        Parameters
        ----------
        error_message : string
            A message describing what went wrong with the test.
        """
        print("Failed: " + self.module  + ": " + error_message)
        self.take_screenshot()
        self.driver.quit()
        exit()

    def keep_trying(self, function, attempts=60, fallback=None, unsatisfactory=None):
        """Continues to try the function without errors for a number of attempts before continuing. This solves
        The problem of Selenium being inconsistent and erroring out because a browser is slow.

        Parameters
        ----------
        assertion : lambda
            A lambda function that should at some point execute successfully.
        attempts : Integer
            The number of attempts to keep trying before letting the test continue
        unsatisfactory : Any
            Value that is unsatisfactory as a return value
        fallback : Any
            The fallback return value if the function did return a satisfactory value within the given
            number of attempts.

        Returns the return value of the function we are trying.
        """
        for i in xrange(attempts):
            try:
                result = function()
                # It will only return if the assertion does not throw an error
                if(result is not unsatisfactory): return result
            except:
                pass
            time.sleep(1)  # This makes the function wait a second between attempts

        return fallback

    def passed(self):
        """Print a generic message when a test has passed
        """
        print("Passed: " + self.module)

    def take_screenshot(self):
        """Take a screenshot with a defined name based on the time and the browser"""
        millis = int(round(time.time() * 1000))
        if(self.driver.name):
            driver_name = self.driver.name
        else:
            driver_name = ""
        self.driver.save_screenshot("screenshots/" + driver_name + "-" + str(millis) + "-screenshots.png")
