import csv
import sys
from KeywordAdsScraper import KeywordAdsScraper

def main():

#check user input
    if (len(sys.argv) > 3 or len(sys.argv) < 1):
        print("usage: main.py inputfile.csv [outputfile.csv]")
        return 0 # stop the program

    inputfile = sys.argv[1]
    outputfile = sys.argv[2] if len(sys.argv) > 2 else "ads.csv"

    # adds .csv appendix if not done by the user
    if ".csv" not in inputfile: inputfile = inputfile + '.csv'
    if ".csv" not in outputfile: outputfile = outputfile + '.csv'

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
    file = open(csv)
    keywords = []

    #sring cleaning
    for keyword in file:
        temp = keyword.replace(";", "")
        temp = temp.replace("\n", "")
        keywords.append(temp)

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
