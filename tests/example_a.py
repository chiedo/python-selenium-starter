"""An example test to show how to structure your tests"""

from tests.base_test import BaseTest


class Test(BaseTest):
    def __init__(self, driver, base_url, module):
        super(Test, self).__init__(driver, base_url, module)

    def run(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver.get(self.base_url)
        if "Google" not in self.driver.title:
            raise Exception("Unable to load google page!")
        # Wrapping any find element call with keep_trying, will make sure selenium keeps making a number of attempts
        # to locate the element before giving up.
        elem = self.keep_trying(lambda: self.driver.find_element_by_name("q"))
        elem.send_keys("BrowerStack")
        elem.submit()
        print self.driver.title
        # No need to quit driver at the end of the test. The run.py file will
        # handle that
