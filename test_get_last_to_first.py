"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_02_one_person_one_friend_diff_last(self):
        param = {'Clare Dunphy': ['Phil Jeffrey']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Jeffrey': ['Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    

    def test_03_one_person_no_friend(self):
        param = {'Clare Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_04_two_person_same_friend(self):
        param = {'Clare Dunphy': ['Phil Jeffrey'], 
                 'Phil Jeffrey': ['Clare Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Jeffrey': ['Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_05_two_person_one_same_friend(self):
        param = {'Clare Dunphy': ['Phil Jeffrey', 'Vincent Jeffrey'], 
                 'Phil Jeffrey': ['Clare Dunphy', 'Vincent Jeffrey']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Jeffrey': ['Phil', 'Vincent']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    def test_06_two_person_two_same_friend(self):
        param = {'Clare Dunphy': ['Phil Jeffrey', 'Vincent Jeffrey', 
                                  'Jack Jeffrey'], 
                 'Phil Jeffrey': ['Clare Dunphy', 'Vincent Jeffrey']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Jeffrey': ['Jack', 'Phil', 'Vincent']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_07_school_example_large_file(self):
        param = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                                      'Rebecca Donaldson-Katsopolis'],
                 'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
                 'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
                 'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                                    'Joey Gladstone']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Katsopolis': ['Jesse'],
                    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
                    'Gladstone': ['Joey'],
                    'Donaldson-Katsopolis': ['Rebecca'],
                    'Gibbler': ['Kimmy'],
                    'Tanner-Fuller': ['DJ']} 
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
if __name__ == '__main__':
    unittest.main(exit=False)
