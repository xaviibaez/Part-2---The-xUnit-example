from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        print(test.wasRun)
        test.run() 
        assert(test.wasRun)
        print(test.wasRun)
        
TestCaseTest("testRunning").run()