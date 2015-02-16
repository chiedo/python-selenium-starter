"""An example test to show how to structure your tests"""

from tests.base_test import BaseTest


class Test(BaseTest):
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
        super(Test, self).__init__(driver, base_url, module)

    def run(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        # No need to quit driver at the end of the test. The run.py file will
        # handle that
