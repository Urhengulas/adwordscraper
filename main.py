import csv
import sys
from KeywordAdsScraper import KeywordAdsScraper

def main():

#check user input

    #check if more than two arguements are given
    if (len(sys.argv) > 3):
        print("usage: main.py inputfile.csv [outputfile.csv]")
        return 0 # stop the program

    try:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2] if len(sys.argv) > 2 else "ads.csv"
    except IndexError:
        print("usage: main.py inputfile.csv [outputfile.csv]")
        return 0 # stop the program

    # adds .csv appendix if not done by the user
    if ".csv" not in inputfile: inputfile += '.csv'
    if ".csv" not in outputfile: outputfile += '.csv'

    # getting the keywords from csv file
    keywords = getKeywordsFromCsv(inputfile)

    # generate an AdWordScraper-Object for each keyword
    keyword_ads_list = [KeywordAdsScraper(key) for key in keywords]

    # Print all Ads in a structured way
    saveAdsAsCsv(keyword_ads_list,outputfile)


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


def getKeywordsFromCsv(csv):
    # reading the csv file
    with open(csv, 'r') as file:
        keywords = []

        #sring cleaning
        for keyword in file:
            keywords.append(keyword.replace(";", "").replace("\n", ""))

        return keywords

def saveAdsAsCsv(adslist, filename):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        #adding header
        writer.writerow(['keyword'] + ['text'] + ['link'])

        for adObject in adslist:
            #iterate through ad dict
            for ad in adObject.ad_list:
                writer.writerow([adObject.title] + [ad['text']] + [ad['ad_link']])


if __name__ == "__main__":
    main()
