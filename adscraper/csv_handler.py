'''handles input and ouput of csv files'''
import csv


def get_keywords(file_name):
    '''gets keywords from csv file'''
    # reading the csv file
    with open(file_name, 'r') as file:
        keywords = []

        # sring cleaning
        for keyword in file:
            temp = keyword.replace(";", "").replace("\n", "")
            keywords.append(temp)

    return keywords


def save_ads(scraper_object, file_name="data/ads.csv"):
    '''saves ads to csv file '''

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        # adding header
        writer.writerow(['keyword'] + ['text'] + ['link'])

        for ad_scraper in scraper_object.scraper_list:
            # iterate through ad dict
            for ad in ad_scraper.ad_list:
                writer.writerow([ad_scraper.title] +
                                [ad['text']] + [ad['ad_link']])
