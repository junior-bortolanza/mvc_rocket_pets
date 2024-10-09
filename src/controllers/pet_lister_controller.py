from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_lister_controller import PetLiserControllerInterface

class PetListerController(PetLiserControllerInterface):
    def __init__(self,  pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_ind_db()
        response = self.__format__response(pets)
        return response

    def __get_pets_ind_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format__response(self, pets: List[PetsTable]) -> Dict:
        formatted_pet = []
        for pet in pets:
            formatted_pet.append({"name": pet.name, "type": pet.type, "id": pet.id})

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pet),
                "attributes": formatted_pet
            }
        }
