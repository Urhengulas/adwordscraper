import csv


def get_keywords(file_name):
    # reading the csv file
    with open(file_name, 'r') as file:
        keywords = []

        # sring cleaning
        for keyword in file:
            temp = keyword.replace(";", "").replace("\n", "")
            keywords.append(temp)

    return keywords


def save_ads(ScraperObject, file_name="data/ads.csv"):

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        # adding header
        writer.writerow(['keyword'] + ['text'] + ['link'])

        for adScraper in ScraperObject.scraper_list:
            # iterate through ad dict
            for ad in adScraper.ad_list:
                writer.writerow([adScraper.title] +
                                [ad['text']] + [ad['ad_link']])
