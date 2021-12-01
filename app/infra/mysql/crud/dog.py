from typing import Any, Dict, Optional

from infra.mysql.crud.base import CRUDBase
from infra.mysql.models.dog import Dog
from schemas.dog import CreateDog, UpdateDog


class CRUDDog(CRUDBase[Dog, CreateDog, UpdateDog]):
    async def get_by_id(self, id: str) -> Optional[Dict[str, Any]]:
        dog = await self.model.get_or_none(id=id)
        return dog


crud_dog = CRUDDog(model=Dog)
