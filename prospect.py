
class Prospect:
    """ Represents a prospect"""

    def __init__(self, first, last, email, uni, major, year, gender,
            hackcount, shirt, dietr, dieto, travel, github, linkedin, site, resume):
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
        self.resume = resume

        self.status = 0 # rejected


    def to_string(self):
        if self.status == 0:
            print(self.first + ' ' + self.last + ': rejected')
        elif self.status == 1: # accepted:
            print(self.first + ' ' + self.last + ': accepted')
        elif self.status == 3: # waitlisted:
            print(self.first + ' ' + self.last + ': waitlisted')

    def deliberate(self, res):
        self.status = res


