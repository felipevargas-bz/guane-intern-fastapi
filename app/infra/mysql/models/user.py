from tortoise import fields
from tortoise.models import Model


class User(Model):
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=250)
    last_modified = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)
