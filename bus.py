

class Bus:
    def __init__(self, number, route=None, timetable=None):
        self.number = number
        self.route = route

        # Should find the solution of None value attribute to timetable
        # which caused by multiple tag in the child of argument timetable.
        if timetable != None:
            self.timetable = timetable
        else:
            self.timetable = ""

    def __str__(self):
        return "number: " + self.number + " \nroute: " + self.route + " \ntimetable: " + self.timetable + "\n"