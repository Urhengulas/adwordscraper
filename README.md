# adwordscraper
Scraper for Google Ads
___

## Table of content

- [Table of content](#table-of-content)
- [About](#about)
- [Getting started](#getting-started)
  - [Development usage](#development-usage)
  - [Production usage](#production-usage)
- [Documentation](#documentation)
- [Collaboration](#collaboration)

## About
Searchig at google, besides the normal search results, also shows you `SearchAds`, which are fitting to the searched term. These differ for different users.  
We assume that there are political SearchAds at Google. Probably they are only shown for specific search terms, to specific people (specific countries, ethnic groups, ...).

We want to validate this hypothesis and try to understand the underlying structure of Google SearchAds.

To do so, we already devloped the [`adscraper`-module](adscraper/), which makes it possible to scrape SearchAds for a list of search terms.
The [`cli.py`](cli.py) makes that functionality available as CLI-tool. It takes a csv-file with search terms as input (default: data/keywords.csv) and outputs a csv-file with all the SearchAds it found for the terms.

## Getting started

**clone repo**
```shell
$ git clone https://github.com/Urhengulas/adwordscraper.git
```

### Development usage
> (directly via python)  
> More convenient for experimenting

```shell
$ # install dependencies
$ make python-setup

$ # run scraper for keywords in `data/keywords.csv`
$ make python-run
```

### Production usage
> (with docker)  
> Makes it easier to scale the scraping.

```shell
$ # create docker image (only repeat after changing sourcecode)
$ make docker-setup

$ # run scraper for keywords in `data/keywords.csv`
$ make docker-run
```

run tests and lint-checking
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
Details about how to collaborate you can find [here](COLLABORATION.md).
