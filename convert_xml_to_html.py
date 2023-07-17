import unittest
import xmlrunner
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    test_suite = unittest.TestLoader().discover(r'C:\Users\rares\PycharmProjects\Project_Carturesti\Tests')
    result = runner.run(test_suite)

    # Convertirea în format HTML
    tree = ET.parse('test-reports')
    tree.write('test-reports\TESTS-TestSuites.html')
