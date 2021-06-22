# Higher level abstract module that handling html string.
# Extract meaningful strings from html string that scraped by scraper module.

from bs4 import BeautifulSoup


class StringExtractor:

    # Constructor
    def __init__(self, html_string=None):
        if html_string is None:
            raise AttributeError("There is no html String!")
        self.total_html_string = html_string
        self.soup = BeautifulSoup(self.total_html_string, "html5lib")

    # Find index of target string in html string.
    # And store all found index to found_line_set, return it.
    def find_tag_strings(self, html_tag_list):
        html_tag_string = self.soup.find_all(html_tag_list)
        return html_tag_string
