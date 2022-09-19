"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_02_one_person_no_club(self):
        param = {'Claire Dunphy': []}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)    

    def test_03_two_person_three_club(self):
        param = {'Vincent Zhu': ['Swim Club', 'Kendo Club'], 
                 'Linh Lang':['Kendo Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
    
    def test_04_two_person_two_club(self):
        param = {'Vincent Zhu': ['Swim Club', 'Kendo Club'], 
                 'Linh Lang':['Kendo Club', 'Study Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)     
    
    def test_05_four_person_seven_club(self):
        param = {'Vincent Zhu': ['Swim Club', 'Kendo Club'], 
                 'Linh Lang':['Kendo Club', 'Study Club'],
                 'Shuai Zhu': ['Kendo Club', 'Math Club'],
                 'Jack Chen': ['Esports Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.75
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)       

    def test_06_school_example_large_file(self):
        param = {'Michelle Tanner': ['Comet Club'],
                 'Danny R Tanner': ['Parent Council'],
                 'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
                 'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
                 'Joey Gladstone': ['Comics R Us', 'Parent Council']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.6
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)     

if __name__ == '__main__':
    unittest.main(exit=False)
