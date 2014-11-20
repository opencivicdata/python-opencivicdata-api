Open Civic Data API Python Wrapper
==================================

This module provides the `opencivicdata.package` module, a set of bindings
to work with the
[Open Civic Data](http://opencivicdata.org/)
[API](http://docs.opencivicdata.org/en/latest/api/index.html).

Quickstart
==========

Most users will want to use the pre-configured Sunlight OCD API client, which
reads your Sunlight API key from the same location as
[python-sunlight](https://github.com/sunlightlabs/python-sunlight) does.

Just set either the `SUNLIGHT_API_KEY` envvar,  or write out your key to
`~/.sunlight.key`.

```python
from opencivicdata.api import SunlightOCDAPI
api = SunlightOCDAPI()
for person in api.people_by_lat_lon(42.35, -71.06):
    print(person)
```

Available Clients
=================

There are 3 built-in clients to the Open Civic Data API bindings, one without
any built-in configuration (the `opencivicdata.api.OCDAPI` class) as a general
use client, one for the Open Civic Data Vagrant deploy client
(the `opencivicdata.api.client.VagrantOCDAPI` class), and one for the Sunlight
Open Civic Data API (the `opencivicdata.api.SunlightOCDAPI` class)


OCDAPI
------

This client takes two arguments, `host` and `apikey`. If the API doesn't
require an API Key, feel free to not pass in `apikey`.

```python
# To test the API server running locally
from opencivicdata.api import OCDAPI
api = OCDAPI(host="http://localhost:8000")
```

VagrantOCDAPI
-------------

This client takes only one optional argument, `apikey`, with a hardcoded host
pointing to `http://10.42.2.102`, the Vagrant API host as seen in the
[vagrant-opencivicdata.org](https://github.com/opencivicdata/vagrant-opencivicdata.org)
config.

SunlightOCDAPI
--------------

This client takes a single optional argument, `apikey`, with a hardcoded host
pointing to `https://api.opencivicdata.org`.

Internally, this will use `SUNLIGHT_API_KEY`, if set, as the API Key. If no
such environment variable is set, it will use the content of
`~/.sunlight.key` as the API key.

If an API key is passed in to `apikey`, this will override all of the above.


Quick Start
===========

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
