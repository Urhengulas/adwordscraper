from bs4 import BeautifulSoup
import urllib3


def get_site_soup(url):
    """Get the Soup of a given Url."""

    # request given url
    http = urllib3.PoolManager()
    r = http.request('get', url)

    # format it nicely and return
    soup = BeautifulSoup(r.data, 'lxml')

    return soup


def parse_for_filter(soup, terms=("li", {"class": "ads-ad"})):
    """Parses the given soup for given filters."""

    # get a list of all the elements, which shall be filtered for
    specific = soup.find_all(terms[0], terms[1])

    # get list of information about the elements and save each in a dictionary
    entry_list = []
    for entry in specific:
        dic = {
            "text": entry.find('a').text,
            "ad_link": entry.find('div', {'class': 'ads-visurl'}).cite.text,
            "html": entry
        }
        entry_list.append(dic)

    return entry_list
