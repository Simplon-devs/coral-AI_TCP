from abc import ABC, abstractmethod


class Server_interface(ABC):

    """Interface for a server class"""

    @abstractmethod
    def app(self):
        """Returns an app object"""
        pass


    @abstractmethod
    def run_test_server(self):
        """Lance le serveur de test"""
        pass


class Data_interface(ABC):

    """Interface pour la base de données/l'API à venir"""
    @abstractmethod
    def init_database(self):

        pass



