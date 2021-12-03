from src.Checker import Checker
from src.Env import Env
from unittest.mock import *
from unittest import TestCase
from datetime import datetime
from assertpy import assert_that


class TestChecker(TestCase):
    @patch.object(Env, 'getTime')
    def test_reminder_before_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2021, 9, 1, 16, 30, 0, 0)
        checker = Checker()
        checker.resetWav()
        checker.reminder()
        assert_that(checker.was_played).is_false()

    @patch.object(Env, 'getTime')
    def test_reminder_after_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2021, 9, 1, 21, 37, 0, 0)
        checker = Checker()
        checker.resetWav()
        checker.reminder()
        assert_that(checker.was_played).is_true()
