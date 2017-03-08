#PART 1 
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import re,sys
import requests
import json


BASE_URL = "http://data-interview.enigmalabs.org"
def main(): 
    progress_bar = 0
    company_list = []
    complete_company_info = []

    # obtain beautiful soup object of the first page
    page_no = 1
    bs = update_bs_object(page_no) 

    '''stop condition for while loop, compatible for variable number of pages, 
    this stops when pagination reaches the end.
    '''
    while bs.table != None:

    # build company list array which consists of all urls in a page
        company_list = get_companies(bs.table)

        for company_url in company_list:
            #append object containing information about current company
            complete_company_info.append(curr_company_info(company_url))

            #handles progress update in mac terminal console
            progress_bar += 1
            update_progress(progress_bar)

        # updates page and gets updated beautifulsoup object,bs
        page_no += 1
        bs = update_bs_object(page_no)
    #write to output json
    write_to_output(complete_company_info)

#progress bar update on terminal
def update_progress(progress):
    sys.stdout.write('\r[{0}] {1}%'.format('#'*(progress/5), progress))
    sys.stdout.flush()

#writes resulting json formatted object to solution.json
def write_to_output(complete_company_info):
    with open('../data/results/solution.json','w') as output:
        json.dump(complete_company_info, output)
    sys.stdout.write("\n")
        
'''function to accept company url, query url by calling get_bs(target),
  and append a json formtted object object which contains pairs of 
  each row of company data table. ie col_arr[0] , col_arr[1] reference
  first and second column of each row respetively
'''
def curr_company_info(company_url):
    company_json = {}
    target = BASE_URL + company_url.replace(' ','%20')
    bs = get_bs(target)
    rows = bs.findAll('tr')
    for row in rows:
        col_arr = row.findAll('td')
        company_json[col_arr[0].text] = col_arr[1].text
    return company_json
    
# this simply returns a beautiful soup object for target url
def get_bs(target):
    html = urlopen(target)
    new_bs = BeautifulSoup(html, 'lxml') 
    return new_bs
    
# function to accept table object and return array of all urls to be queried  
def get_companies(table):
    company_urls = []
    page_url_array = table.findAll('a', href = re.compile("(/companies/)"))  
    for link  in page_url_array:
        company_urls.append(link['href'])
    return company_urls
    
#update until end of pagination(supports varying number of paginations)
def update_bs_object(page_no):
    next_page = BASE_URL + "/companies/?page="+ str(page_no)
    html = urlopen(next_page)
    new_bs = BeautifulSoup(html, 'lxml')
    return new_bs

            
if __name__ == "__main__":
    main()
        
             