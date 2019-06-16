import pytest
from adscraper import csv_handler


def test_get_keywords():
    # test if file gets open correctly
    assert csv_handler.get_keywords('tests/test.csv')

    # test if Error gets raised when file not exists
    with pytest.raises(FileNotFoundError):
        csv_handler.get_keywords('foo.csv')

    # test if right keywords get extracted
    keywords = csv_handler.get_keywords('tests/test.csv')
    test_keywords = ["This ", "Are", "TEST", "keywords"]
    assert keywords == test_keywords
