import requests.exceptions
from lib import scraper, gui
from bs4 import BeautifulSoup
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
        self.bus_dict = {}

    def read_timetable(self):
        # Make soup
        soup = BeautifulSoup(self.html_string, "lxml")
        # All bus timetable information are located between <td> tags.
        td = soup.find_all('td')
        # Between time of the bus that departing different stations,
        # there is string which contain departure station name.
        # But it is covered with <span> tags and needs to be uncovered(unwrap).
        for departure in soup.findAll('span'):
            departure.unwrap()

        # Store all read timetable data in bus_list in way of Bus class.
        for i in range(0, len(td), 3):
            self.bus_dict[td[i].text] = Bus(td[i].text, td[i + 1].text, td[i + 2].text)

    def get_bus(self):
        while True:
            bus_number = input("Please input bus number >> ")
            try:
                wanted_bus = self.bus_dict[bus_number]
            except KeyError:
                print("There is no such bus!")
                print("Check bus number again")
            else:
                return wanted_bus

    def make_gui(self):
        g = gui.Gui()
        for bus in self.bus_dict:
            g.make_bus_button(self.bus_dict[bus])
        g.show_bus_info(self.bus_dict["100"])
        g.execute()



a = CCBusScraper("http://www.chuncheon-pti.kr/index.php?mp=p2_4_1")
a.read_timetable()
a.make_gui()