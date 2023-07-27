import unittest
import HtmlTestRunner

from Tests.tests import Tests

class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        smoketest = unittest.TestSuite()
        smoketest.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Tests)])

        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Report tests Carturesti', report_name='First report', combine_reports=True
        )
        runner.run(smoketest)

