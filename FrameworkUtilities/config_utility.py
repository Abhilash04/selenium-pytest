"""
This module contains config utility functions.
"""

from traceback import print_stack
from configparser import ConfigParser


class ConfigUtility:
    """
    This class includes basic reusable config_helpers.
    """
    def __init__(self, config_path):
        self.config_path = config_path

    def load_properties_file(self):
        """
        This method loads the properties/ini file
        :return: this method returns config reader instance.
        """

        config = None
        try:
            # noinspection PyBroadException
            config = ConfigParser()
            config.read(self.config_path)

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
            print_stack()

        return config
