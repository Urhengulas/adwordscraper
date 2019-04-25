# adwordscraper
Scraper for Google Ads
___

## Table of content

- [About](#about)
- [Getting started](#getting-started)
  - [development usage](#development-usage)
  - [production usage](#production-usage)
- [Documentation](#documentation)
- [Collaboration](#collaboration)

## About
Searchig at google besides the normal search results also shows you `SearchAds`, which are fitting to the searched term. Also there are different SearchAds for different users.  
We assume that there are also political SearchAds. Probably they are only shown for specific search terms, to specific people (specific countries, ethnic groups, ...).

We want to validate our hypothesis and try to understand the underlying structure of Google SearchAds.

To do so, we already devloped the `adscraper`-module, which makes it possible to scrape SearchAds for a list of search terms.
The `cli.py` makes that functionality available as CLI-tool. It takes a csv-file with search terms as input (default: data/keywords.csv) and outputs a csv-file with all the SearchAds it found for the terms.

## Getting started

**clone repo**
```shell
$ git clone https://github.com/Urhengulas/adwordscraper.git
```

### development usage
> (directly via python)  
> More convenient for experimenting

```shell
$ # install dependencies
$ make python-setup

$ # run scraper for keywords in `data/keywords.csv`
$ make python-run
```

### production usage
> (with docker)  
> Makes it easier to scale the scraping.

```shell
$ # create docker image (only repeat after changing sourcecode)
$ make docker-setup

$ # run scraper for keywords in `data/keywords.csv`
$ make docker-run
```

**_(optional) run tests and lint-checking_**
```shell
$ make test
$ make lint
```

**_(optional) open jupyter notebook (with env-ads-kernel)_**
```shell
$ make notebok
```

## Documentation
Documenation about the adscraper module you can find [here](adscraper/DOCUMENTATION.md).

## Collaboration
Details about how to collaborate you can find [here](docs/COLLABORATION.md).
