from . import DataManager


class SingletonException(Exception):
    pass


class UniversalDataConnection:
    """
    Singleton that holds instance of data manager class for universal access.
    """
    __instance = None

    def __init__(self, data_manager: DataManager = None):
        if UniversalDataConnection.__instance is not None:
            raise SingletonException
        else:
            self.__data_connection = data_manager
            UniversalDataConnection.__instance = self

    @staticmethod
    def get_instance():
        if UniversalDataConnection.__instance is None:
            raise Exception('UniversalDataConnection was not created at startup.')
        return UniversalDataConnection.__instance

    @property
    def data_connection(self) -> DataManager:
        return self.__data_connection

    @data_connection.setter
    def data_connection(self, data_manager):
        self.__data_connection = data_manager  # This supports changing the data source, for better or for worse
