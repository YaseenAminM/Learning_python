# # Test File this file is for production

# # pyLint
# # pyFlakes

# # PEP 8


# import unittest
# import main


# class TestMain(unittest.TestCase):
#     def setUp(self):
#         print("about to test function")

#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 15)

#     def test_do_stuff2(self):
#         """
#         TEST 1
#         """
#         test_param = "adadwwa"
#         result = main.do_stuff(test_param)
#         self.assertIsInstance(result, ValueError)

#     def test_do_stuff3(self):
#         test_param = None
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, "please enter number")

#     def test_do_stuff4(self):
#         test_param = ''
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, "please enter number")

#     def test_do_stuff5(self):
#         test_param = 'awdawdawd'
#         result = main.do_stuff(test_param)
#         self.assertTrue(isinstance(result, Exception))

#     def tearDown(self):
#         print("cleaning up")


# if __name__ == '__main__':
#     unittest.main()


import unittest
import exercise


class TestScript(unittest.TestCase):
    def test_input(self):
        result = exercise.run_guess_game(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = exercise.run_guess_game(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = exercise.run_guess_game(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = exercise.run_guess_game(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
