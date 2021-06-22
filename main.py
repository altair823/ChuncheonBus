
import requests.exceptions

import lib.string_extractor
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

        # the set of bus timetables.
        self.bus_list = set()

    def get_total_string(self):
        return self.html_string

    def _find_buses_from_html(self):
        _string_extractor = lib.string_extractor.get_extractor(self.html_string)
        _string_extractor.set_start_target("<TD>")
        _string_extractor.set_end_target("</TD>")
        return _string_extractor.find_string()

    def find_buses(self):
        self.bus_list = self._find_buses_from_html()
        for i in self.bus_list:
            print(self.html_string[i[0]:i[1]])


a = CCBusScraper("http://www.chuncheon-pti.kr/index.php?mp=p2_4_1")
#print(a.get_total_string())
#print(a.find_buses())
a.find_buses()