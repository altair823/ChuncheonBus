import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(os.path.abspath("bus_gui.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class BusGUI(QMainWindow, form_class) :
    def __init__(self, bus_dict) :
        super().__init__()
        self.setupUi(self)

        self.bus_dict = bus_dict

        self.bus_list.currentIndexChanged.connect(self.print_route)
        self.bus_list.currentIndexChanged.connect(self.print_timetable)

    def add_a_bus(self, a_bus):
        self.bus_list.addItem(a_bus)

    def add_bus_all(self):
        for bus_key in self.bus_dict.keys():
            self.add_a_bus(bus_key)

    def print_route(self):
        self.bus_route_label.setText(self.bus_dict[self.bus_list.currentText()].route)

    def print_timetable(self):
        self.bus_timetable_label.setText(self.bus_dict[self.bus_list.currentText()].timetable)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = BusGUI()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()