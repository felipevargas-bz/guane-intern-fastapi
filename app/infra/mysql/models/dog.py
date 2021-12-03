from tortoise import Model, fields


class Dog(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    picture = fields.CharField(max_length=100)
    is_adopted = fields.BooleanField()
    create_date = fields.DatetimeField(auto_now=True)
    update_date = fields.DatetimeField(auto_now_add=True)
    id_user = fields.IntField()
