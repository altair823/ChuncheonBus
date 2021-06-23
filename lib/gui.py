from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QHBoxLayout, QVBoxLayout
from bus import Bus


class Gui:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.all = QVBoxLayout()
        self.buttons_layout = QHBoxLayout()
        self.info_layout = QHBoxLayout()
        self.button_row = 1

    def make_bus_button(self, a_bus):
        if type(a_bus) != Bus:
            raise AttributeError("Not Bus Class!")
        btn = QPushButton(a_bus.number)
        btn.setCheckable(False)
        self.buttons_layout.addWidget(btn)
        self.button_row += 1

    def show_bus_info(self, a_bus):
        route_label = QLabel(a_bus.route)
        timetable_label = QLabel(a_bus.timetable)
        self.info_layout.addWidget(route_label, 2)
        self.info_layout.addWidget(timetable_label, 3)

    def execute(self):
        self.window.setLayout(self.buttons_layout)
        self.window.setLayout(self.info_layout)
        self.window.show()
        self.app.exec()

