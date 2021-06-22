
import requests.exceptions

from lib import scraper
from lib import string_extractor


class CCBusScraper:

    def __init__(self, url_string=None):
        self.url = url_string
        try:
            _scraper = scraper.Scraper(self.url)
        except requests.exceptions.InvalidURL:
            print("Invalid URL Exception! Abort program. ")
            exit(1)
        self.header = _scraper.get_header()
        self.html_string = _scraper.get_html_string()

    def get_total_string(self):
        return self.html_string

    def find_buses(self):
        _string_extractor = string_extractor.StringExtractor(self.html_string)
        _string_extractor.set_target("<TD>")
        return _string_extractor.find_string()


a = CCBusScraper("http://www.chuncheon-pti.kr/index.php?mp=p2_4_1")
#print(a.get_total_string())
print(a.find_buses())