from typing import Dict
from abc import ABC, abstractmethod

class PetListerControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: int) -> Dict:
        pass
