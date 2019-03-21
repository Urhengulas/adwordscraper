import sys
from SearchAdsScraper import SearchAdsScraper


def main():
    """
    make the scraper via CLI available 
    """

    # check user input
    # check if more than two arguements are given
    if (len(sys.argv) > 3):
        print("usage: python main.py inputfile.csv [outputfile.csv]")
        return 0  # stop the program

    try:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2] if len(sys.argv) > 2 else "ads.csv"
    except IndexError:
        print("usage: python main.py inputfile.csv [outputfile.csv]")
        return 0  # stop the program

    # adds .csv appendix if not done by the user
    if ".csv" not in inputfile:
        inputfile += '.csv'
    if ".csv" not in outputfile:
        outputfile += '.csv'

    # generate the SearchAdsScraper-Object with the <inputfile>
    Scraper = SearchAdsScraper(inputfile)

    # let it scrape
    Scraper.scrape()

    # print result
    print(Scraper)

    # save results to <outputfile>
    Scraper.save_to_csv(outputfile)


if __name__ == "__main__":
    main()
