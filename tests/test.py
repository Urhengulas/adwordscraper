from adscraper import scraper
from bs4 import BeautifulSoup


def test_parse_for_filter():
    # getting mocked soup
    with open("tests/sample.html", "r") as doc:
        soup = BeautifulSoup(doc, 'lxml')

    ret = scraper.parse_for_filter(soup)

    for entry in ret:
        entry["html"] = str(entry["html"])

    wanted = ([{'text': 'I am an ad. Yay.',
                'ad_link': 'www.giffits.de/Beutel/Bedrucken',
                'html': '<li class="ads-ad">\n<a>I am an ad. Yay.</a>\n<div class="ads-visurl">\n<cite class="UdQCqe">www.giffits.de/Beutel/Bedrucken</cite>\n</div>\n</li>'},
               {'text': 'I am also an fancy ad. Woop woop.',
                'ad_link': 'www.moritz.dev',
                'html': '<li class="ads-ad">\n<a>I am also an fancy ad. Woop woop.</a>\n<div class="ads-visurl">\n<cite class="UdQCqe">www.moritz.dev</cite>\n</div>\n</li>'}])

    assert ret == wanted, "TestError: scraper.parse_for_filter() didn't pass the ... test."

    return "scraper.parse_for_filter() passed all tests."


def main():
    print("# Started testing scraper.parse_for_filter()")
    print("... {}".format(test_parse_for_filter()))


if __name__ == "__main__":
    main()
