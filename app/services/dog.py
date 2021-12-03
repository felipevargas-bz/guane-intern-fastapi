from infra.mysql.crud.dog import crud_dog
from infra.services.base_service import BaseService


class DogService(BaseService):
    async def get_by_id(self, id: int):
        dog = await self._queries.get_by_id(id=id)
        return dog


dog_service = DogService(crud=crud_dog)
