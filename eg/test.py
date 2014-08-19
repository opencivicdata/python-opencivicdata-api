from opencivicdata.api import OCDAPI

client = OCDAPI(host="http://localhost:8000")

for org in client.organizations():
    print(client.organization(org['id']))
