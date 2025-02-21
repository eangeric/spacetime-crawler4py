import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
    url_list = list()

    # Check for empty sites
    if url == None or resp == None or resp.raw_response.content == None:
        return url_list
    
    # Verify response status is valid
    if not resp.status == 200:
        # Placeholder for error checking
        print(resp.status)
        return url_list
    
    # Convert text to usable format
    raw_text = resp.raw_response.text
    parsed_text = BeautifulSoup(raw_text,'html.parser')

    # Check unique pages
    #   Unique pages function?
    # Count words, check for longest document
    #   Maybe add a function for this?
    # Count 50 most common words w/o stop words
    #   Word counter function
    # Count subdomains

    # Extract links from text
    
    temp_links = list() # Holds unchecked links

    for item in parsed_text.find_all('a'):
        links = item.get('href') # Returns a list of links
        if is_valid(links):
            temp_links.append(links)
    # Break down links into sections


    # Verify that links point to websites within our domain
    # using updated is_valid function

    # Remove the fragment from end of link

    # Check for duplicates

    # Check for traps

    # If link passes all tests, add it to the url_list


    return url_list

## TODO:
'''
    List of valid domains:
    *.ics.uci.edu/*
    *.cs.uci.edu/*
    *.informatics.uci.edu/*
    *.stat.uci.edu/*
'''

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
