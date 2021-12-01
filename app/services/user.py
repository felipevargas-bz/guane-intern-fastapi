from infra.mysql.crud.user import crud_user
from infra.services.base_service import BaseService


class UserService(BaseService):
    async def get_by_email(self, email: str):
        user = await self._queries.get_by_username(email=email)
        return user


user_service = UserService(crud=crud_user)
