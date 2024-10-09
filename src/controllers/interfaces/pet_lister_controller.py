from typing import Dict
from abc import ABC, abstractmethod

class PetLiserControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: int) -> Dict:
        pass
