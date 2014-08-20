from opencivicdata.api import OCDAPI

api = OCDAPI(host="http://localhost:8000")

r = api.people()
r.print_debug()
