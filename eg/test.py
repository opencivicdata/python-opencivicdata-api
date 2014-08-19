from opencivicdata.api import OCDAPI

client = OCDAPI(host="http://localhost:8000")

print(client.organizations())
