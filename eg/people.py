from opencivicdata.api.client import SunlightOCDAPI
api = SunlightOCDAPI()
people = api.people()
while people.has_next():
    for person in people:
        print(person['name'])
    people = people.next()
