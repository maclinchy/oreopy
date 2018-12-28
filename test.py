from base import Model
from fields import TextField, IntegerField

class Album(Model):
    title = TextField()
    artist = TextField()
    year = IntegerField()


