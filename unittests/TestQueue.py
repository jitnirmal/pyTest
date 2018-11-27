import unittest
from .. import datastructures


def calc(a, op, b):
    if op not in '+-/*':
        return None, 'Operator must be +-/*'
    try:
        if op=='+':
            result=a+b
        elif op=='-':
            result=a-b
        elif op=='/':
            result=a/b
        else:
            result=a*b
    except Exception as e:
        return None,e.__class__.__name__
    return result,str(result)

#
#   define the test class
#
class testCalc(unittest.TestCase):

    def testSimpleAdd(self):
        result,msg = calc(1,'+',1)
        self.assertEqual(result,2.0)

    def testLargeProduct(self):
        result,msg = calc(123456789.0, '*',987654321.0)
        self.assertEqual(result, 1.2193263111263526e+17)
    
    def testDivByZero(self):
        result,msg = calc(6,'/',0.0)
        self.assertEqual(msg,'ZeroDivisionError')
#
#   create the test suite
#
TestSuite = unittest.TestSuite()
#
#   add tests to the suite
#
TestSuite.addTest(testCalc("testSimpleAdd"))
TestSuite.addTest(testCalc("testLargeProduct"))
TestSuite.addTest(testCalc("testDivByZero"))
#
#   create the test runner
#
runner = unittest.TextTestRunner()
#
#   execute the tests
#
runner.run(TestSuite)