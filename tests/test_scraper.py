from bs4 import BeautifulSoup
from adscraper import scraper
import pickle


def test_request_website():
    # test if request_website() returns anything
    test_http = scraper.request_website("example.com")

    assert test_http, "RequestError: Requesting the website failed."

    # test if request_website() returns the right thing
    test_http_data = test_http.data

    with open("tests/sample.http", "rb") as doc:
        true_http_data = pickle.load(doc)

    assert test_http_data == true_http_data, "ContentError: Content of the request \
        data doesn't fit the expectation."


def test_get_site_soup():
    with open("tests/sample.html", 'r') as doc:
        test_soup = scraper.get_site_soup(doc)

    with open("tests/sample.soup", 'rb') as doc:
        true_soup = pickle.load(doc)

    assert test_soup == true_soup, "TestError: scraper.get_site_soup() didn't pass the test."

    return "scraper.get_site_soup() passed all tests."
