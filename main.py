import sys

import requests.exceptions
from PyQt5.QtWidgets import QApplication

from lib import scraper
from lib.gui import BusGUI
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



a = CCBusScraper("http://www.chuncheon-pti.kr/index.php?mp=p2_4_1")
a.read_timetable()

# QApplication : 프로그램을 실행시켜주는 클래스
app = QApplication(sys.argv)

# WindowClass의 인스턴스 생성
myWindow = BusGUI(a.bus_dict)

myWindow.add_bus_all()

# 프로그램 화면을 보여주는 코드
myWindow.show()

# 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
app.exec_()