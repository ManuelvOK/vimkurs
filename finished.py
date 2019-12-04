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

def subscribe(attendeename, course):
    course.attendees.append(Attendee(attendeename))

def subscribe_attendee(course, attendee):
    course.attendees.append(attendee)

def unsubscribe_attendee(course, attendee):
    course.attendees.remove(attendee)

if __name__ == '__main__':
    courses = []
    courses.append(Course("vim kurs", 3))
    courses.append(Course("gnu emacs curse", 333))
    courses.append(Course("advanced c-kurs limited", 3))
    courses.append(Course("python vortrag", 3))

    attendees = ["Hannes", "Christian", "Olli", "Justin", "Sarah", "Friedrich", "Max", "Ronnie", "Fabian", "Silvie", "Felix"]

    for attendee in attendees:
        subscribe(attendee, courses[0]);

    for course in courses:
        print(course.type)
        for attendee in course.attendees:
            attendee.print()
        print()
