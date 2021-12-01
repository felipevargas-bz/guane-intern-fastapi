from app.infra.postgres.crud.bank import crud_bank
from app.infra.services.base_service import BaseService


class BankService(BaseService):
    async def get_by_username(self, username: str):
        bank = await self._queries.get_by_username(name=username)
        return bank


bank_service = BankService(crud=crud_bank)
