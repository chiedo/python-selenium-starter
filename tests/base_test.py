class BaseTest(object):
    """A test class for the others to inherit to preven duplicate code"""
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def test_success(self, test_name):
        print "%s ran successfully" % (test_name)
        print "\n"

    def test_failure(self, test_name):
        # At this point other things can happen such as screenshots, etc.
        print "%s did not run successfully" % (test_name)
        print "\n"
