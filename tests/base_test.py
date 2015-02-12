"""A test class for others to inherit to prevent duplicate code."""

import time


class BaseTest(object):
    def __init__(self, driver, base_url):
        """Init

        Parameters
        ----------
        driver : object
            The selenium web driver
        base_url : string
            The base url of the web page we will be visiting.
        """
        self.driver = driver
        self.base_url = base_url

    def passed(self, file_name):
        """Print a generic message when a test has passed

        Parameters
        ----------
        file_name : string
            The name of the file that is currently being executed.
        """
        print("Passed: " + file_name)

    def failed(self, error_message):
        """Print a generic message when a test has failed, take a screenshot and end the test.
        Parameters
        ----------
        error_message : string
            A message describing what went wrong with the test.
        """
        print("Error: " + error_message)
        self.take_screenshot()
        self.driver.quit()
        exit()

    def take_screenshot(self):
        """Take a screenshot with a defined name based on the time and the browser"""
        millis = int(round(time.time() * 1000))
        self.driver.save_screenshot(self.driver.name + "-" + millis + "-screenshots.png")
