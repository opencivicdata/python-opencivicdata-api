Open Civic Data API Python Wrapper
==================================

This module provides the `opencivicdata.package` module, a set of bindings
to work with the
[Open Civic Data](http://opencivicdata.org/)
[API](http://docs.opencivicdata.org/en/latest/api/index.html).


Basic Usage
-----------

[Register for a Sunlight API Key](http://sunlightfoundation.com/api/accounts/register/),
and put the API key in a file at `~/.sunlight.key`, or export it into the `env`
as `SUNLIGHT_API_KEY`.

Iterate over a page of people
-----------------------------

```python
from opencivicdata.api import SunlightOCDAPI
api = SunlightOCDAPI()
for person in api.people():
    print(person['name'])
```

Iterate over all people
-----------------------

```python
from opencivicdata.api import SunlightOCDAPI
api = SunlightOCDAPI()
people = api.people()
while people.has_next():
    for person in people:
        print(person['name'])
    people = people.next()
```

Query people by lat/lon
------------------------

```python
from opencivicdata.api import SunlightOCDAPI
api = SunlightOCDAPI()
for person in api.people_by_lat_lon(42.35, -71.06):
    print(person)
```
