
import requests.exceptions

from lib import scraper, string_extractor
from bus import Bus


class CCBusScraper:

    def __init__(self, url_string=None):
        self.url = url_string
        try:
            _scraper = scraper.Scraper(self.url)
        except requests.exceptions.InvalidURL:
            print("Invalid URL Exception! Abort program. ")
            exit(1)
        else:
            self.header = _scraper.get_header()
            self.html_string = _scraper.get_html_string()

        # the set of bus timetable data.
        self.bus_list = {}

    def find_buses(self):
        _string_extractor = string_extractor.StringExtractor(self.html_string)
        td_tagged = _string_extractor.find_tag_strings('td')
        td_tagged_list = []
        for i in td_tagged:
            td_tagged_list.append(i.string)

        #100
        a_bus = Bus(td_tagged_list[0], td_tagged_list[1], td_tagged_list[2])
        self.bus_list["100"] = a_bus

        #100-1
        a_bus = Bus(td_tagged_list[3], td_tagged_list[4], td_tagged_list[5])
        self.bus_list["100-1"] = a_bus

        #200
        a_bus = Bus(td_tagged_list[6], td_tagged_list[7], td_tagged_list[8])
        self.bus_list["200"] = a_bus
        print(self.bus_list["200"])
        #print(self.bus_list["200"])


a = CCBusScraper("http://www.chuncheon-pti.kr/index.php?mp=p2_4_1")
#print(a.get_total_string())
#print(a.find_buses())
a.find_buses()