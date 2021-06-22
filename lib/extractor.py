# Higher level abstract module that handling html string.
# Extract meaningful strings from html string that scraped by scraper module.
# So this module needs the scraper module before executed.

import scraper


class StringExtractor:

    def __init__(self, url_string):
        self.url = url_string
        _scraper = scraper.Scraper(self.url)
        self.header = _scraper.get_header()
        self.html_string = _scraper.get_html_string()

    def get_total_string(self):
        return self.html_string


