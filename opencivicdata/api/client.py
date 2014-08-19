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

    def _get_object(self, entity_id, **kwargs):
        """
        Get an Object in the Open Civic Data API by it's ID, which
        is a valid API path from the root of the app. This method
        is the means through which all other detail methods hit the
        API.
        """
        return self._query(
            "GET",
            entity_id,
            handler=OCDDictResult,
            **kwargs
        )

    def _get_list(self, *args, **kwargs):
        """
        Get the list response from the Open Civic Data API by its
        API rest path. This method is the means through with all
        other list endpoints hit the API.
        """
        return self._query(
            "GET",
            *args,
            handler=OCDListResult,
            **kwargs
        )

    # List methods.

    def jurisdictions(self, **kwargs):
        """
        Get all jurisdictions, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._get_list("jurisdictions", **kwargs)

    def people(self, **kwargs):
        """
        Get all people, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._get_list("people", **kwargs)

    def votes(self, **kwargs):
        """
        Get all votes, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._get_list("votes", **kwargs)

    def events(self, **kwargs):
        """
        Get all events, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._get_list("events", **kwargs)

    def organizations(self, **kwargs):
        """
        Get all organizations, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._get_list("organizations", **kwargs)

    def bills(self, **kwargs):
        """
        Get all bills, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._get_list("bills", **kwargs)

    def divisions(self, **kwargs):
        """
        Get all divisions, with params **kwargs.

        All fields will be used to filter on, with the exception
        of the special ``fields`` param, which will limit the
        response fields.
        """
        return self._get_list("divisions", **kwargs)

    # Detail methods.

    def jurisdiction(self, jurisdiction_id, *args, **kwargs):
        """
        Get an organization ``jurisdiction_id`` from the API,
        filtering on ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get_object(jurisdiction_id, *args, **kwargs)

    def person(self, person_id, *args, **kwargs):
        """
        Get a person ``person_id`` from the API, filtering on
        ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get_object(person_id, *args, **kwargs)

    def vote(self, vote_id, *args, **kwargs):
        """
        Get a vote ``vote_id`` from the API,
        filtering on ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get_object(vote_id, *args, **kwargs)

    def event(self, event_id, *args, **kwargs):
        """
        Get an event ``organization_id`` from the API,
        filtering on ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get_object(event_id, *args, **kwargs)

    def organization(self, organization_id, *args, **kwargs):
        """
        Get an organization ``organization_id`` from the API,
        filtering on ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get_object(organization_id, *args, **kwargs)

    def bill(self, bill_id, *args, **kwargs):
        """
        Get a bill ``bill_id`` from the API, filtering on
        ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get_object(bill_id, *args, **kwargs)

    def division(self, division_id, *args, **kwargs):
        """
        Get a bill ``division_id`` from the API, filtering on
        ``**kwargs``.

        There is no validation done on the object ID. If the object
        ID is of a different type, this method will return that
        object without validating.
        """
        return self._get_object(division_id, *args, **kwargs)
