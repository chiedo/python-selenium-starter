"""An example test to show how to structure your tests"""

from tests.base_test import BaseTest


class Test(BaseTest):
    def __init__(self, driver, base_url, module):
        super(Test, self).__init__(driver, base_url, module)

    def run(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        # No need to quit driver at the end of the test. The run.py file will
        # handle that
