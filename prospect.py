
class Prospect:
    """ Represents a prospect"""

    def __init__(self, first, last, email, uni, major, year, gender,
            hackcount, shirt, dietr, dieto, travel, github, linkedin, site):
        self.first = first
        self.last = last
        self.email = email
        self.uni = uni
        self.major = major
        self.year = year
        self.gender = gender
        self.hackcount = hackcount
        self.shirt = shirt
        self.dietr = dietr
        self.dieto = dieto
        self.travel = travel
        self.github = github
        self.linkedin = linkedin
        self.site = site

        self.status = False


    def to_string(self):
        if self.status:
            print(self.first + ' ' + self.last + ': accepted')
        else:
            print(self.first + ' ' + self.last + ': rejected')

    def deliberate(self, res):
        self.status = res


