# adwordscraper
Scraper for Google Ads
___

## Hypothesis
There are different Google Ads for different users.

## Approach
We want to validate that hypothesis and try to understand the underlying structure.
To do so, we want to develop a crowd-sourcing tool, which scrapes for Google Ads with the different Google Identities of all users.

## Open Questions
- How do the results differ by
    - user
    - location

## Possible Obstacles
- to scrape google searches is officially prohibited --> google.com/robots.txt
- How to make Google think that the search is done by the people and not by the scraper.

## Usage
### standard usage
The standard way to use the scraper is via docker:
#### create docker image
```shell
$ make setup
```
#### run scraper for keywords in keywords.csv-file
```shell
$ make run
```

### python script usage
You can also use the via scraper via the python script:
#### create python virtualenv and install dependencies 
(+ register ipython kernel)
```shell
$ make python-setup
```
#### run scraper for keywords in keywords.csv-file
```shell
$ make python-run
```

#### (optional) open jupyter notebook
```shell
$ make notebok
```