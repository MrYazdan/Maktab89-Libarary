from core.models import BaseModel
from peewee import CharField


class User(BaseModel):
    username = CharField(max_length=32, unique=True)
    password = CharField(max_length=32, _hidden=True)

    def __str__(self):
        return f"<U:{self.id}> username: {self.username}"

