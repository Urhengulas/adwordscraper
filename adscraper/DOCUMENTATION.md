# Documentation for `adscraper` module

## Table of Content

- [Documentation for `adscraper` module](#documentation-for-adscraper-module)
  - [Table of Content](#table-of-content)
  - [`SearchAdsScraper`](#searchadsscraper)
    - [`SearchAdsScraper.SearchAdsScraper()`](#searchadsscrapersearchadsscraper)
      - [Parameters](#parameters)
      - [Examples](#examples)
      - [Attributes](#attributes)
      - [Methods](#methods)
    - [`SearchAdsScraper._KeywordScraper()`](#searchadsscraperkeywordscraper)
      - [Parameters](#parameters-1)
      - [Examples](#examples-1)
      - [Attributes](#attributes-1)
      - [Methods](#methods-1)
  - [`scraper`](#scraper)
    - [functions](#functions)
  - [`csv_handler`](#csvhandler)
    - [functions](#functions-1)

## `SearchAdsScraper`

### `SearchAdsScraper.SearchAdsScraper()`
> class SearchAdsScraper.SearchAdsScraper(inputfile)
 
An `SearchAdsScraper` is a container, which contains a list of `_KeywordScraper`-objects for all the keywords in a given `inputfile`.

#### Parameters

| parameter | dtype | description |
| :--- | :--- | :--- |
| inputfile | `str` | Path to the csv-file with the input-keywords

#### Examples
```python
from SearchAdsScraper import SearchAdsScraper

Scraper = SearchAdsScraper("data/keywords.csv")
```

While initializing it first generates a list of all keywords (`self.keyword_list`) and then automatically starts scraping them for the first time (`self.scraper_list`).

#### Attributes

| attribute | dtype | description |
| :--- | :--- | :--- |
| input_file_name | `str` | Path to the csv-file with the input-keywords
| keyword_list | `list` | List of search keywords (extracted from inputfile)
| scraper_list | `list` | List of `_KeywordScraper`-objects for each search keword

#### Methods

| method | description |
| :--- | :--- |
| `scrape()` | Scrapes for all keywords in `self.keyword_list`
| `save_to_csv(file_name)` | Saves all ads to the csv file file_name
| `__str__()` | Provides representation if e.g. `print()` is called on the object

### `SearchAdsScraper._KeywordScraper()`
> (private) class SearchAdsScraper._KeywordScraper(keyword)

An `_KeywordScraper` is a container for all the Google SearchAds for one single search keyword.  
It is only for internal usage of the `SearchAdsScraper`!

#### Parameters

| parameter | dtype | description |
| :--- | :--- | :--- |
| keyword | `str` | Search Keyword for which shall be scraped

#### Examples
```python
from SearchAdsScraper import _KeywordScraper

KeywordScraper = _KeywordScraper("Print bags")
```

While initializing it first generates the to-be-searched url  (`self.url`) and then automatically starts scraping for all ads (`self.ad_list`) for the first time.

#### Attributes

| attribute | dtype | description |
| :--- | :--- | :--- |
| title | `str` | Search Keyword
| url | `str` | To-be-searched url
| ad_list | `list` | List of all ads which where found for `self.title`

#### Methods

| method | description |
| :--- | :--- |
| `generate_url()` | Generates the to-be-searched url
| `get_ad_list(file_name)` | Scrapes `self.url` for ads


## `scraper`
> module which provides functionalitites related to scraping to the `SearchAdsScraper` and `_KeywordScraper`

### functions 

| method | return | description |
| :--- | :--- | :--- |
| `request_website(url)` | `urllib3.response.HTTPResponse` | Sends `GET`-request to `url`
| `get_site_soup(http_request_data)` | `bs4.BeautifulSoup` | Converts `http_request_data` to an `bs4.BeautifulSoup`-obj
| `parse_for_filter(soup, terms=("li", {"class": "ads-ad"}))` | `list` of `dict`s | Extracts the ads (with the pattern `terms`) from `soup`

## `csv_handler`
> module which provides functionalities related to handling csv files to the `SearchAdsScraper` and `_KeywordScraper`

### functions

| method | return | description |
| :--- | :--- | :--- |
| `get_keywords(file_name)` | `list` | Extracts keywords from csv-file `file_name`
| `save_to_csv(scraper_list, file_name="data/ads.csv")` | | Saves `scraper_list` to csv-file `file_name`