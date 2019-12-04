class Attendee:
    def __init__(self, name):
        self.name = name

    def printh(self):
        print(self)

    def __str__(self):
        return "Attendee<{}>".format(self.name)
