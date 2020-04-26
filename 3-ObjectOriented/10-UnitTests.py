# 2 basic unit testing tools: pylint and unittest
# pylint: this is a library which looks at the code and reports styling issues or invalid code, cmd: pip install pylint
#         from command line, use pylint script.py to run test on script.py

# unittest: built-in library which allows to test your own programs and check if you're getting desired output
#           here, we have to create new test.py file which we execute to run the test on script.py

# Example unittest:
# We will test the Test.py script in this unittest:
# ???? WHY does it run all functions in TestThisScriptUsingUnitTest.py although we have test cases only for fun1()????

import unittest
import TestThisScriptUsingUnitTest


class MyUnitTest(unittest.TestCase):
    def test_case1_for_one_word(self):      # test case 1
        test_this_text = 'Amol'             # the string to be tested
        test_result = TestThisScriptUsingUnitTest.fun1(test_this_text)  # result of the test
        MyUnitTest.assertEqual(self, test_result, (1, 3))               # check the test result and expected result
        #                                                                 order of args does not matter

    def test_case2_for_multi_words(self):   # test case 2
        test_this_text = 'My name is Amol'  # the string to be tested
        test_result = TestThisScriptUsingUnitTest.fun1(test_this_text)  # result of the test
        MyUnitTest.assertEqual(self, (2, 10), test_result)       # check the test result and expected result
        #                                                                 order of args does not matter


if __name__ == '__main__':         # To ensure running main() only when we run from current script and not if we
    #                                call this script in another script
    unittest.main()                # This main() method from unittest built-in package is mandatory to run the test case
