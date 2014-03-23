from pkg_resources import resource_string
from jsonschema import validate
import logging

class client(object):
    """
    A REST client for the Web-HDFS API

    Aims to be a replacement for `hdfs dfs`
    """

    def __init__(self, name_node_host, name_node_port, user_name):
        self.log  = logging.getLogger( 'wdfs.client' )
        self.host = name_node_host
        self.port = name_node_port
        self.user = user_name

    def get_home_folder(self):
        """
        Returns the home folder location for the constructed object
        """

        try:
            response = {}
            path_schema = resource_string( 'wdfs.resources.schemas', 'path.json' )
            self.log.trace(
                'retrieved path schema: %(path)s' % {
                'path': path_schema
            })

            validate( response, path_schema )
        except ValidationError as error:
            self.log.error(
                'Unexpected response: %(error)s' % {
                'error': error
            })
