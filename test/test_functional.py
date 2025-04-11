import unittest
import pandas as pd
from mainclass import PlayerScoreAnalysis
from test.TestUtils import TestUtils
import os

class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = PlayerScoreAnalysis({
        'player_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'player_name': ['John', 'Michael', 'Sarah', 'Anna', 'David', 'Emily', 'George', 'Lily', 'James', 'Tom'],
        'score': [65, 40, 55, 90, 70, 60, 45, 80, 35, 50]
    })
        cls.test_obj = TestUtils()

    def test_create_player_series(self):
        """Test if the player series is created correctly."""
        try:
            obj = isinstance(self.analysis.score_series, pd.Series) and len(self.analysis.score_series) == 10
            self.test_obj.yakshaAssert("TestCreatePlayerSeries", obj, "functional")
            print("TestCreatePlayerSeries = Passed" if obj else "TestCreatePlayerSeries = Failed")
        except:
            self.test_obj.yakshaAssert("TestCreatePlayerSeries", False, "functional")
            print("TestCreatePlayerSeries = Failed")
    
    def test_get_score_for_player(self):
        """Test if the score for player 3 is fetched correctly."""
        obj = self.analysis.get_score_for_player(3) == 55
        self.test_obj.yakshaAssert("TestGetScoreForPlayer", obj, "functional")
        print("TestGetScoreForPlayer = Passed" if obj else "TestGetScoreForPlayer = Failed")
    
    def test_update_score_for_player(self):
        """Test if the score for player 3 is updated correctly."""
        self.analysis.update_score_for_player(3, 80)
        obj = self.analysis.get_score_for_player(3) == 80
        self.test_obj.yakshaAssert("TestUpdateScoreForPlayer", obj, "functional")
        print("TestUpdateScoreForPlayer = Passed" if obj else "TestUpdateScoreForPlayer = Failed")
    
    def test_get_players_above_threshold(self):
        """Test if players with score above 50 are fetched correctly."""
        try:
            result = self.analysis.get_players_above_threshold(50)
            obj = len(result) == 6  # Expecting 6 players
            self.test_obj.yakshaAssert("TestGetPlayersAboveThreshold", obj, "functional")
            print("TestGetPlayersAboveThreshold = Passed" if obj else "TestGetPlayersAboveThreshold = Failed")
        except:
            self.test_obj.yakshaAssert("TestGetPlayersAboveThreshold", False, "functional")
            print("TestGetPlayersAboveThreshold = Failed")

    def test_save_updated_score_series(self):
        """Test if the updated score series is saved to a CSV file."""
        self.analysis.save_updated_score_series("updated_scores.csv")
        obj = os.path.exists("updated_scores.csv")
        self.test_obj.yakshaAssert("TestSaveUpdatedScoreSeries", obj, "functional")
        print("TestSaveUpdatedScoreSeries = Passed" if obj else "TestSaveUpdatedScoreSeries = Failed")
