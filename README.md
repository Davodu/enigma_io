
## Overview
This repo contains two python scripts. A [CSV parser](https://github.com/Davodu/enigma_io/blob/master/CSVTest/csv_test.py) and a [Web scraper](https://github.com/Davodu/enigma_io/blob/master/WebScrape/web_scrape.py) 

## CSV Parser
This script transforms an [input file](https://github.com/Davodu/enigma_io/blob/master/data/CSVFiles/test.csv) into a desired [output file](https://github.com/Davodu/enigma_io/blob/master/data/results/solution.csv) by performing the following operations:
- Normalizes the bio field into space delimited strings
- Changes state abbreviations to state names based on a dictionary generated from a [state abbreviation](https://github.com/Davodu/enigma_io/blob/master/data/CSVFiles/state_abbreviations.csv) file.
- Seperates invalid dates from valid ones and transforms valid dates to ISO 8601 standard.<br><hr>
- Run command from CVSTest directory : ``` python csv_test.py```
- Required module: Python [csv](https://docs.python.org/2/library/csv.html)

## Web Scraper
This [script](https://github.com/Davodu/enigma_io/blob/master/WebScrape/web_scrape.py) scrapes a [sample site](http://data-interview.enigmalabs.org/companies/) and [outputs](https://github.com/Davodu/enigma_io/blob/master/data/results/solution.json) its data in JSON.Overview: 
- Iterates until end of pagination
- For each page, queries each company url and extracts data in json format.
- Appends each company info to a global array and generates this [output file](https://github.com/Davodu/enigma_io/blob/master/data/results/solution.json) <br><hr>
- Run command from WebScrape directory : ``` python web_scrape.py```
- Libraries used: 
    * Python's robust HTML parser [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    * Python [json](https://docs.python.org/2/library/json.html) module.
