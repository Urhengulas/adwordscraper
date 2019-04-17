from . import scraper
from . import csv_handler


class SearchAdsScraper():
    """TODO: write definition"""

    def __init__(self, file_name):
        self.input_file_name = file_name
        self.keyword_list = csv_handler.get_keywords(self.input_file_name)
        self.scrape()

    def scrape(self):
        """Create a list of _KeywordScraper-objects for each keyword"""
        self.scraper_list = [_KeywordScraper(key) for key in self.keyword_list]

    def save_to_csv(self, file_name):
        csv_handler.save_ads(self.scraper_list, file_name)

    def __str__(self):
        """Print all Ads in a structured way."""

        ret = ""

        for keyword_scraper in self.scraper_list:

            ret += "### Keyword: {}\n".format(keyword_scraper.title)

            if not keyword_scraper.ad_list:
                ret += "There are no ads.\n"
            else:
                for ad in keyword_scraper.ad_list:
                    ret += "#\tText: {}\n\tLink: {}\n\n".format(
                        ad["text"], ad["ad_link"]
                    )

        return ret


class _KeywordScraper():
    """Scraper for one specific keyword"""

    def __init__(self, keyword):
        self.title = keyword
        self.url = self.generate_url()
        self.ad_list = self.get_ad_list()

    def generate_url(self):
        """Generate the url to scrape for"""

        keyword = self.title.lower()
        split = keyword.split(" ")
        merge = "+".join(split)
        link = "http://www.google.de/search?q=" + merge

        return link

    def get_ad_list(self):
        """Scrape for ads for the given url
        and save them in ad_list"""

        http_request = scraper.request_website(self.url)
        soup = scraper.get_site_soup(http_request.data)
        ad_list = scraper.parse_for_filter(
            soup, terms=("li", {"class": "ads-ad"}))
        return ad_list
