from opencivicdata.api import OCDAPI

api = OCDAPI(host="http://localhost:8000")

response = api.people()
while response:
    print(response)
    response = response.next()
