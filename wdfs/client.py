from pkg_resources import resource_string
import logging
import json
import requests
from jsonschema import ValidationError
from jsonschema import validate

class client(object):
    """
    A REST client for the Web-HDFS API

    Aims to be a replacement for `hdfs dfs`
    """

    def __init__(self, host, port, user):
        self.log  = logging.getLogger( 'wdfs.client' )
        self.user = user
        self.url = 'http://%(host)s:%(port)d/webhdfs/v1' % {
              'host': host
            , 'port': port
        }

    def _service_call(self, params, schema):
        """
        Make a REST call with the specified params
        And validates against the schema given
        """
        try:
            http_response = requests.get( self.url, params=params )

            self.log.debug(
                'retrieved response: %(response)s' % {
                'response': http_response.text
            })

            json_response = json.loads( http_response.text )
            print json_response
            validate( json_response, schema )
            return json_response

        except ValidationError as error:
            self.log.error(
                'Unexpected response: %(error)s' % {
                'error': error
            })

    def get_home_folder(self):
        """
        Returns the home folder location for the constructed object
        """

        params = {
            'user.name': self.user
          , 'op': 'GETHOMEDIRECTORY'
        }

        path_schema = resource_string( 'wdfs.resources.schemas', 'path.json' )
        self.log.debug(
            'retrieved path schema: %(path)s' % {
            'path': path_schema
        })

        return self._service_call(params, json.loads(path_schema) )[u'Path']

