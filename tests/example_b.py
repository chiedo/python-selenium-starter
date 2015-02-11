from tests.base_test import BaseTest


class Test(BaseTest):
    def __init__(self, driver, base_url):
        super(Test, self).__init__(driver, base_url)

    def run(self):
        self.test_success("Example B")
        # No need to quit driver at the end of the test. The run.py file will
        # handle that
