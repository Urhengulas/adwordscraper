from KeywordAdsScraper import KeywordAdsScraper


def getKeywordsFromCsv(csv):
    # reading the csv file
    file = open(csv)
    keywords = []

    #sring cleaning
    for keyword in file:
        temp = keyword.replace(";", "")
        temp = temp.replace("\n", "")
        keywords.append(temp)

    return keywords


def main():
    # getting the keywords from csv file
    keywords = getKeywordsFromCsv("test.csv")

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
