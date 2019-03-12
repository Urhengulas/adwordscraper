from KeywordAdsScraper import KeywordAdsScraper


def main():
    # list of keywords we are scraping for
    keywords = ["refugee", "eu", "europe", "smartphone",
                "google", "beutel", "bedrucken", "ads", "vote", "brexit"]

    # generate an AdWordScraper-Object for each keyword
    keyword_ads_list = [KeywordAdsScraper(key) for key in keywords]

    # Print all Ads in a structured way
    print_keyword_ads_list(keyword_ads_list)


def print_keyword_ads_list(keyword_ads_list):
    """Print all Ads in a structured way."""
    for keyword_ad in keyword_ads_list:
        print("### Keyword: {}".format(keyword_ad.title))

        if not keyword_ad.ad_list:
            print("There are no ads.")
        else:
            for ad in keyword_ad.ad_list:
                print("#\tText: {}\n\tLink: {}".format(
                    ad["text"], ad["ad_link"]))
        print()


if __name__ == "__main__":
    main()
