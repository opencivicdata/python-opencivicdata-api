from opencivicdata.api import OCDAPI
import statistics


api = OCDAPI(host="http://localhost:8000")

response = api.people()
times = []
while response:
    times.append(response.debug['time']['seconds'])
    response = response.next()


print("Total: {}".format(len(times)))
print("Min:   {}".format(min(times)))
print("Max:   {}".format(max(times)))
print("Mean:  {}".format(statistics.mean(times)))
