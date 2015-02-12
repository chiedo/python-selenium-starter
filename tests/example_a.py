"""An example test to show how to structure your tests"""

from tests.base_test import BaseTest


class Test(BaseTest):
    def __init__(self, driver, base_url):
        """Init

        Parameters
        ----------
        driver : object
            The selenium web driver
        base_url : string
            The base url of the web page we will be visiting.
        """
        super(Test, self).__init__(driver, base_url)

    def run(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver.get(self.base_url)
        if "Google" not in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("BrowerStack")
        elem.submit()
        print self.driver.title
        self.passed("example_a.py")
        # No need to quit driver at the end of the test. The run.py file will
        # handle that
