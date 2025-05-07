import unittest
from mainclass import PlayerScoreAnalysis
from test.TestUtils import TestUtils
import pandas as pd


class ExceptionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = PlayerScoreAnalysis({
        'player_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'player_name': ['John', 'Michael', 'Sarah', 'Anna', 'David', 'Emily', 'George', 'Lily', 'James', 'Tom'],
        'score': [65, 40, 55, 90, 70, 60, 45, 80, 35, 50]
    })
        cls.test_obj = TestUtils()
    
    def test_invalid_player_id(self):
        """Test if an invalid player ID is handled correctly."""
        try:
            player = self.analysis.get_score_for_player(999)  # Non-existent player ID
            if not player:
                self.test_obj.yakshaAssert("TestInvalidPlayerID", True, "exceptional")
                print("TestInvalidPlayerID = Passed")
            else:
                self.test_obj.yakshaAssert("TestInvalidPlayerID", False, "exceptional")
                print("TestInvalidPlayerID = Failed")
        except KeyError:
            self.test_obj.yakshaAssert("TestInvalidPlayerID", True, "exceptional")
            print("TestInvalidPlayerID = Passed")

    def test_invalid_column_access(self):
        """Test if accessing a non-existent player column throws an error."""
        try:
            self.analysis.score_series["Invalid_Player"]
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", False, "exceptional")
            print("TestInvalidColumnAccess = Failed")            
        except KeyError:
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", True, "exceptional")
            print("TestInvalidColumnAccess = Passed")
        except:
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", False, "exceptional")
            print("TestInvalidColumnAccess = Failed")