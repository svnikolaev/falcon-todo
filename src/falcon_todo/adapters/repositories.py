from abc import ABC, abstractmethod
from embrace import pool


class AbstractRepository(ABC):
    _connection = None

    @abstractmethod
    def get(self):
        raise NotImplementedError


class EmbraceRepository:

    def __init__(self, connection):
        self._connection = connection


class UsersRepo(AbstractRepository):

    def get(self):
        ...
