from opencivicdata.api import OCDAPI

client = OCDAPI(host="http://localhost:8000")

for org in client.organizations(
    memberships__person__name__icontains="John",
):
    print(org)
