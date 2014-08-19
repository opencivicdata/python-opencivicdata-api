from opencivicdata.api import OCDAPI

api = OCDAPI(host="http://localhost:8000")

for person in api.people():
    print(person)
