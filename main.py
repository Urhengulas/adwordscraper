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



    # print result
    print(Scraper)


if __name__ == "__main__":
    main()
