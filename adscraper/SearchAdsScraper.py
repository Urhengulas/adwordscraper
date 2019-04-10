from . import scraper
from . import csv_handler


class SearchAdsScraper():
    keyword_list = []
    scraper_list = []
    input_file_name = ""
    output_file_name = "ads.csv"

    def __init__(self, file_name):
        self.input_file_name = file_name
        self.keyword_list = csv_handler.get_keywords(self.input_file_name)

    def scrape(self):
        self.scraper_list = [_KeywordScraper(key) for key in self.keyword_list]

    def save_to_csv(self, file_name=""):
        if not file_name:
            file_name = self.output_file_name

        csv_handler.save_ads(self, file_name)

    def __str__(self):
        """Print all Ads in a structured way."""
        for scraper in self.scraper_list:

            print("### Keyword: {}".format(scraper.title))

            if not scraper.ad_list:
                print("There are no ads.")
            else:
                for ad in scraper.ad_list:
                    print(
                        "#\tText: {}\n\tLink: {}\n".format(
                            ad["text"], ad["ad_link"]
                        )
                    )
        return ""


class _KeywordScraper():
    title = ""
    url = ""
    ad_list = []

    def __init__(self, keyword):
        self.title = keyword
        self.url = self.generate_url()
        self.ad_list = self.get_ad_list()

    def generate_url(self):
        keyword = self.title.lower()
        split = keyword.split(" ")
        merge = "+".join(split)
        link = "http://www.google.de/search?q=" + merge
        return link

    def get_ad_list(self):
        soup = scraper.get_site_soup(self.url)
        ad_list = scraper.parse_for_filter(
            soup, terms=("li", {"class": "ads-ad"}))
        return ad_list
