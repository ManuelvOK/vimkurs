# Copyright
from attendee import Attendee

class Course:
    def __init__(self, course_type, length):
        self.type = course_type
        self.length = length
        self.attendees = []

    def activate(self):
        self.active = true

    def overrun(self):
        self.length += 1

def subscribe(course, attendeename):
    course.attendees.append(Attendee(attendeename))

if __name__ == '__main__':
    courses = []
    courses.append(Course("vim kurs", 3))
    courses.append(Course("gnu emacs curse", 333))
    # TODO: subscribe the following attendees:
    # Hannes
    # Christian
    # Olli
    # Justin
    # Sarah
    # Friedrich
    # Max
    # Ronnie
    # Fabian
    # Sylvie
    # Felix

    # TODO: subscribe the following attendees to an emacs course:
    # Felix
    # Sarah
    # Fabian

    # TODO: create two new courses for "advanced c-kurs limited" and "pyton vortrag"

    # TODO: write another subscribe function that takes an attendee and not just a name

    # TODO: write an unsubscribe function. HINT: you remove an element e from a list l with l.remove(e)

    # TODO: rewrite the course subscriptions as a for loop

    # TODO: uncomment the following code and fix the issues until it runs

    #for course in courses:
    #    print(course.type)
    #    for attendee in course.attendees:
    #        attendee.print()
    #    print()
