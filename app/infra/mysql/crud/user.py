from typing import Any, Dict, Optional

from infra.mysql.crud.base import CRUDBase
from infra.mysql.models import User
from schemas.user import CreateUser, UpdateUser


class CRUDUser(CRUDBase[User, CreateUser, UpdateUser]):
    async def get_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        user = await self.model.get_or_none(email=email)
        return user


crud_user = CRUDUser(model=User)
