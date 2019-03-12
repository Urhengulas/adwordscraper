import scraper


class KeywordAdsScraper():
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
            soup, filter=("li", {"class": "ads-ad"}))
        return ad_list
