import sys
import webbrowser
import re
from prospect import Prospect

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

refer = ['Miran Solanki', 'Lawrence Wong', 'Carlos Vasquez', 'Sean Kim', 
        'Zachary Petzinger', 'Jeffrey Tai', 'Samuel Bekker', 
        'Hiroka Tamura', 'Debparna Pratiher', 'Karthik Bharathala', 'Srinath Goli', 'Carlo Cruz-Albrecht', 'Jennifer Kim',
        'Shashank Guduru', 'Clarice Wong', 'Clarice Wong', 'David Chang', 'Miguel Acevedo',
        'Anushka Singh', 'Christian Fahrney', 'Disha Bendre', 'Anny Hsu', 'Brandon Luong', 
        'Donald Pickney', 'Stephanie Chang', 'Rachel Lee', 'Alex Fu', 'David Lin', 'Joanne Wang', 'Pooja Rajkumar',
        'Mary Serafin', 'Karissa Tom', 'Sanil Gupta', 'Vishan Menon', 'Vishaal Prasad', 'Kushal Cuttari']

#p = Prospect('name', 'davis', 10)
#p.to_string()
def process_prospect(p):
    p = re.split(',(?=(?:[^"]*\"[^"]*\")*[^"]*$)',p)
    #print('first:\t\t' + p[1])
    #print('last:\t\t' + p[2])
    #print('email:\t\t' + p[3])
    #print('uni:\t\t' + p[4][1:-1])
    #print('major:\t\t' + p[5][1:-1])
    #print('year:\t\t' + p[6])
    #print('gender:\t\t' + p[7])
    #print('hacks attended:\t' + p[8])
    #print('shirt size:\t' + p[9])
    #print('diet restrict:\t' + p[10])
    #print('diet option:\t' + p[11][1:-1])
    #print('help travel?:\t' + p[12])
    #print('github:\t\t' + p[21])
    #print('linkedin:\t' + p[22])
    #print('website:\t' + p[23])
    #print('gender:'+ p[7])

    # make new person
    per = Prospect(p[1], p[2], p[3], p[4][1:-1], p[5][1:-1], p[6], p[7].lower(), p[8], p[9], p[10], p[11][1:-1], p[12], p[21], p[22], p[23], p[20])
    return(per)

def display_person(per):
    print('first:\t\t' + per.first)
    print('last:\t\t' + per.last)
    print('email:\t\t' + per.email)
    print('uni:\t\t' + per.uni)
    print('major:\t\t' + per.major)
    print('year:\t\t' + per.year)
    print('gender:\t\t' + per.gender)
    print('hacks attended:\t' + per.hackcount)
    print('shirt size:\t' + per.shirt)
    print('diet restrict:\t' + per.dietr)
    print('diet option:\t' + per.dieto)
    print('help travel?:\t' + per.travel)
    print('github:\t\t' + per.github)
    print('linkedin:\t' + per.linkedin)
    print('website:\t' + per.site)
    print('resume:\t' + per.resume)
    if per.resume != '':
        webbrowser.get(chrome_path).open(per.resume)


def display_total(accept, reject, waitlist, num_female, num_male, num_other_gender, num_fresh,
        num_soph, num_junior, num_senior, num_davis, count, total):
    print('\n')
    print(str(num_female) + ' females accepted')
    print(str(num_male) + ' males accepted')
    print(str(num_other_gender) + ' other genders accepted')
    print(str(num_davis) + ' from Davis')
    print(str(total) + ' total')
    print('\n')
    print(str(len(accept)) + ' accepted out of ' + str(count) + ' prospects')

def deliberate(prospect_list, total, start):
    accept = []
    reject = []
    waitlist = []
    count = 0
    num_female = 0
    num_male = 0
    num_other_gender = 0
    num_fresh = 0
    num_soph = 0
    num_junior = 0
    num_senior = 0
    num_davis = 0

    i = start
    while i < len(prospect_list):
        per = prospect_list[i]
        result = ''

        if per.first + ' ' + per.last in refer or per.gender == 'female':
            result = 'a'
        else:
            display_person(per)
            display_total(accept, reject, waitlist, num_female, num_male, num_other_gender, num_fresh, num_soph, num_junior, num_senior, num_davis, count, total)
            result = input("Accept, Waitlist, or Reject? (a or w or r or b or q): ")
            #result = 'r'

        count = count + 1

        if result.lower() == 'q':
            return(accept)
        if result.lower() == 'b': 
            # alter stats
            if i == 0:
                count = count - 1
                continue
            prev = prospect_list[max(i - 1, 0)]
            # update gender
            if prev.gender == 'female':
                num_female = num_female - 1
            elif prev.gender == 'male':
                num_male = num_male - 1
            else:
                num_other_gender = num_other_gender - 1

            # update year
            if prev.year == 1:
                num_fresh = num_fresh - 1
            elif prev.year == 2:
                num_soph = num_soph - 1
            elif prev.year == 3:
                num_junior = num_junior - 1
            else:
                num_senior = num_senior - 1

            # update davis
            if 'davis' in prev.uni:
                num_davis = num_davis - 1

            if accept and accept[-1].first == prev.first and accept[-1].last == prev.last:
                accept.pop()
            if reject and reject[-1].first == prev.first and reject[-1].last == prev.last:
                reject.pop()
            if waitlist and waitlist[-1].first == prev.first and waitlist[-1].last == prev.last:
                waitlist.pop()

            count = count - 2

            i = max(i - 1, 0)
            continue

        if result.lower() == 'a':
            per.deliberate(1)
            accept.append(per)

            # update gender
            if per.gender == 'female':
                num_female = num_female + 1
            elif per.gender == 'male':
                num_male = num_male + 1
            else:
                num_other_gender = num_other_gender + 1

            # update year
            if per.year == 1:
                num_fresh = num_fresh + 1
            elif per.year == 2:
                num_soph = num_soph + 1
            elif per.year == 3:
                num_junior = num_junior + 1
            else:
                num_senior = num_senior + 1

            # update davis
            if 'davis' in per.uni.lower():
                num_davis = num_davis + 1

            # modify stats
        elif result.lower() == 'w':
            per.deliberate(2)
            waitlist.append(per)
        else:
            per.deliberate(1)
            reject.append(per)

        i = i + 1

    return(accept)

def process_data(accepted):
    prospect_list = []
    total = 0

    # read in file
    with open('report.csv') as txt:
        # parse file
        applicants = txt.readlines()

        total = len(applicants) - 1

        # add each person
        for person in applicants[1:]:
            per = process_prospect(person)
            prospect_list.append(per)

    #for person in prospect_list:
    #    print(person.first + ' ' + person.last)

    emails = []
    

    for i in accepted:
        for person in prospect_list:
            if i == person.first + ' ' + person.last:
                print('hit')
                emails.append(person.email)
        # find the corresponding person in prospect_list
        # save their info

    return(list(set(emails)))

def finish(result):
    with open('contact.txt', 'w') as out:
        for email in result:
            out.write(email + '\n')

if __name__ == '__main__':
    print('usage: python3 contact.py accept_list')
    start = 0

    accepted = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as acc:
            a = acc.readlines()
            accepted = a
        #start = int(sys.argv[1])

    print(accepted[0:10])
    for i in range(0, len(accepted)):
        print(accepted[i].strip())
        accepted[i] = accepted[i].strip()

    result = process_data(accepted)

    finish(result)
