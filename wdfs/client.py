import logging

class client(object):
    """
    A REST client for the Web-HDFS API

    Aims to be a replacement for `hdfs dfs`
    """

    def __init__(self, name_node_host, name_node_port, user_name):
        self.host = name_node_host
        self.port = name_node_port
        self.user = user_name

        self.home = self.get_home_folder()

    def get_home_folder(self):
        """
        Returns the home folder location for the constructed object
        """
        pass
