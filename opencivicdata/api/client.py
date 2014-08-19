from opencivicdata.api.service import Service
from opencivicdata.api.result import OCDListResult, OCDDictResult


class OCDAPI(Service):
    """
    Open Civic Data API wrapper.
    """

    def __init__(self, host=None, apikey=None):
        """
        Simple constructor. Invokes the setup routines. This is
        where we can override default behavior if we need.
        """
        self.setup(host=host, apikey=apikey)

    def _get(self, entity_id, **kwargs):
        """
        Get an Object in the Open Civic Data API by it's ID, which
        is a valid API path from the root of the app. This method
        is the means through which all other methods hit the API.
        """
        return self._query(
            "GET",
            entity_id,
            handler=OCDDictResult,
            **kwargs
        )

    def organizations(self, **kwargs):
        """
        Get all organizations, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._query(
            "GET",
            "organizations",
            handler=OCDListResult,
            **kwargs
        )

    def organization(self, organization_id, *args, **kwargs):
        """
        Get an organization ``organization_id`` from the API,
        filtering on ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get(organization_id, *args, **kwargs)

    def person(self, person_id, *args, **kwargs):
        """
        Get a person ``person_id`` from the API, filtering on
        ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get(person_id, *args, **kwargs)

    def bill(self, bill_id, *args, **kwargs):
        """
        Get a bill ``bill_id`` from the API, filtering on
        ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get(bill_id, *args, **kwargs)

    def vote(self, vote_id, *args, **kwargs):
        """
        Get a vote ``vote_id`` from the API,
        filtering on ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get(vote_id, *args, **kwargs)

    def event(self, event_id, *args, **kwargs):
        """
        Get an event ``organization_id`` from the API,
        filtering on ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get(event_id, *args, **kwargs)
