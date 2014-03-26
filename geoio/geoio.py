#
#  Created by Felix Wittmann on 2014-03-26
#  Copyright (c) 2014 happy bits GmbH. All rights reserved.
#

import json
import logging

import requests

logger = logging.getLogger(__name__)


class GeoioException(Exception):
    """Class for all exceptions thrown by the geoio API."""

    def __init__(self, error_message):
        super(GeoioException, self).__init__()
        self.error_message = error_message

    def __str__(self):
        return "GeoioException: %s" % repr(self.error_message)

class GeoioClient(object):
    """Representing a connection to the geoio API."""

    APIKEY = None
    API_ENDPOINT = "api.geo.io/v1"
    USE_SSL = False

    def __init__(self, apikey):
        """Creates a GeoioClient instance.

        :Parameters:
         - `apikey` - your geoio apikey
        
        """
        self.APIKEY = apikey



    def _api_url(self, path):
        """Helper method for create request-url
            :Parameters:
             - `path` - api-method

            :Returns:
                The request url
        """
        if self.USE_SSL:
            protocol = "https"
        else:
            protocol = "http"


        return "%s://%s/%s/" %(protocol, self.API_ENDPOINT, path)


    def _api_header(self):
        """Helper method for create request-headers

            :Returns:
                The request headers
        """
        return {"X-Auth-Token": self.APIKEY, "Content-Type": "application/json"}

    def _api_query(self, path, data=None, method="GET"):
        """Helper method for making API calls
            :Parameters:
             - `path` - api-method
             - `data` - `Dictionary` of data to send to the server in request-body or (if `method` is GET) in querystring
             - `method` - HTTP request type

            :Returns:
                A `Dictionary` with the result of the API-Call
        """
        if method is "GET":
            response = requests.get(self._api_url(path), params=data, headers=self._api_header())
        elif method is "POST":
            response = requests.post(self._api_url(path), data=json.dumps(data), headers=self._api_header())
        elif method is "PUT":
            response = requests.post(self._api_url(path), data=json.dumps(data), headers=self._api_header())
        elif method is "DELETE":
            response = requests.post(self._api_url(path), data=json.dumps(data), headers=self._api_header())

        response = json.loads(response.text)

        if "status" not in response:
            raise GeoioException("Unknown Error.")

        if response["status"] == "ZERO_RESULTS":
            return []

        if response["status"] != "OK":
            raise GeoioException(response["message"])

        return response["results"]


    def geocoding(self, query):
        """Geocode one or more addresses
            :Parameters:
             - `query` - string or list of addresses

            :Returns:
                A `Dictionary` with the result of the API-Call
        """
        if type(query) is str or type(query) is unicode:
            result = self._api_query("geocoding", {"query":query})
        elif type(query) is list:
            request_body = []
            for item in query:
                request_body.append({"query": item})
            result = self._api_query("geocoding/batch", request_body, "POST") 
        else:
            result = self._api_query("geocoding/batch", query, "POST") 
        return result



    def reverse_geocoding(self, query):
        """Reverse-Geocode one or more posititons
            :Parameters:
             - `query` - dict or list of positions

            :Returns:
                A `Dictionary` with the result of the API-Call
        """
        if type(query) is dict:
            result = self._api_query("reverse-geocoding", query)
        elif type(query) is list:
            result = self._api_query("reverse-geocoding/batch", query, "POST") 
        return result

