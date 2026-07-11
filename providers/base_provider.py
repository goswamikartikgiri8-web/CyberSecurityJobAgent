from abc import ABC, abstractmethod
from typing import List
from models.job import Job


class BaseProvider(ABC):
    """
    Base class for all job providers.
    """

    name: str = "Unknown"

    @abstractmethod
    def fetch_jobs(self) -> List[Job]:
        """Return a list of Job objects."""
        raise NotImplementedError