import sys
from adscraper.SearchAdsScraper import SearchAdsScraper


def main():
    """make the scraper via CLI available"""

    inputfile, outputfile = handle_input(sys.argv)

    # generate the SearchAdsScraper-Object with the <inputfile>
    # (scrapes automatically)
    Scraper = SearchAdsScraper(inputfile)

    # print result via SearchAdsScraper.__str__()
    print(Scraper)

    # save results to <outputfile>
    Scraper.save_to_csv(outputfile)


def handle_input(sys_argv):
    check_number_of_arguments(sys_argv)

    inputfile, outputfile = get_filenames_from_arguments(sys_argv)

    inputfile = check_csv_extension(inputfile)
    outputfile = check_csv_extension(outputfile)

    check_name(inputfile)

    return inputfile, outputfile


def check_number_of_arguments(sys_argv):
    """check if more than two arguements are given"""

    assert (len(sys_argv) >= 1 and len(sys_argv) <= 3), \
        "usage: python cli.py inputfile.csv [outputfile.csv]"

def check_name(file):
    """ check if given file does exit """
    try:
        open(file)
    except FileNotFoundError:
        print('This file does not exist')
        exit()


def get_filenames_from_arguments(sys_argv):
    try:
        inputfile = sys.argv[1]

        if len(sys_argv) > 2:
            outputfile = sys.argv[2]
        else:
            outputfile = "ads.csv"
    except IndexError:
        assert False, "usage: python cli.py inputfile.csv [outputfile.csv]"

    return inputfile, outputfile


def check_csv_extension(filename):

    if ".csv" not in filename:
        filename += '.csv'

    return filename


if __name__ == "__main__":
    main()
