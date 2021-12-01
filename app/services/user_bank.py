from app.infra.postgres.crud.user_bank import crud_user_bank
from app.infra.services.base_service import BaseService


class UserBankService(BaseService):
    async def get_relation(self):
        object_relation = await self._queries.get_relation()
        return object_relation

    async def get_relation_by_user(self, user_id):
        relation_by_user = await self._queries.get_relation_by_user(user_id)
        return relation_by_user

    async def get_relation_by_bank(self, bank_id):
        relation_by_bank = await self._queries.get_relation_by_bank(bank_id)
        return relation_by_bank

    async def get_one_relation(self, bank_id, user_id):
        one_relation = await self._queries.get_one_relation(bank_id, user_id)
        return one_relation


user_bank_service = UserBankService(crud=crud_user_bank)
