import unittest

from csc131 import lab02


class Lab02TestCase(unittest.TestCase):
    """
    Unit tests for the `csc131.lab02` module.
    """

    def setUp(self):
        """
        Set up the test fixture; this is executed before each unit test executes.
        :return: None
        """
        self.use_recursion_flag = True
        self.use_iteration_flag = False
        self.NEGATIVE_FIB = -1
        self.ZERO_FIB = 0
        self.LOW_FIB = 1
        self.MEDIUM_FIB = 7
        self.HIGH_FIB = 20

    def tearDown(self):
        """
        Clean up the test fixture; this executed after each unit test has executed.
        :return: None
        """
        self.use_recursion_flag = None
        self.use_iteration_flag = None
        self.NEGATIVE_FIB = None
        self.ZERO_FIB = None
        self.LOW_FIB = None
        self.MEDIUM_FIB = None
        self.HIGH_FIB = None

    def test_fact_negative_n_iteratively(self):
        expected_value = -1
        actual_value = lab02.fact(-1, self.use_iteration_flag)
        self.assertEqual(expected_value, actual_value)

    def test_fact_negative_n_recursion(self):
        expected_value = -1
        actual_value = lab02.fact(-1)
        self.assertEqual(expected_value, actual_value)

    def test_fact_zero_n_iteratively(self):
        expected_value = 1
        actual_value = lab02.fact(0, self.use_iteration_flag)
        self.assertEqual(expected_value, actual_value)

    def test_fact_zero_n_recursion(self):
        expected_value = 1
        actual_value = lab02.fact(0)
        self.assertEqual(expected_value, actual_value)

    def test_fact_one_iteratively(self):
        expected_value = 1
        actual_value = lab02.fact(1, self.use_iteration_flag)
        self.assertEqual(expected_value, actual_value)

    def test_fact_one_recursion(self):
        expected_value = 1
        actual_value = lab02.fact(1)
        self.assertEqual(expected_value, actual_value)

    def test_fact_five_iteratively(self):
        expected_value = 120
        actual_value = lab02.fact(5, self.use_iteration_flag)
        self.assertEqual(expected_value, actual_value)

    def test_fact_five_recursion(self):
        expected_value = 120
        actual_value = lab02.fact(5)
        self.assertEqual(expected_value, actual_value)

    def test_fact_forty_iteratively(self):
        expected_value = 815915283247897734345611269596115894272000000000
        actual_value = lab02.fact(40, self.use_iteration_flag)
        self.assertEqual(expected_value, actual_value)

    def test_fact_forty_recursion(self):
        expected_value = 815915283247897734345611269596115894272000000000
        actual_value = lab02.fact(40)
        self.assertEqual(expected_value, actual_value)

    def test_negative_fib(self):
        expected_value = -1
        actual_value = lab02.fib(self.NEGATIVE_FIB)
        self.assertEqual(expected_value, actual_value)

    def test_zero_fib(self):
        expected_value = -1
        actual_value = lab02.fib(self.ZERO_FIB)
        self.assertEqual(expected_value, actual_value)

    def test_low_fib(self):
        expected_value = 1
        actual_value = lab02.fib(self.LOW_FIB)
        self.assertEqual(expected_value, actual_value)

    def test_medium_fib(self):
        expected_value = 13
        actual_value = lab02.fib(self.MEDIUM_FIB)
        self.assertEqual(expected_value, actual_value)

    def test_high_fib(self):
        expected_value = 6765
        actual_value = lab02.fib(self.HIGH_FIB)
        self.assertEqual(expected_value, actual_value)


#
# Script entry-point enforcement.
#
if __name__ == '__main__':
    unittest.main()
