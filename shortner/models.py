from django.db import models
from mongoengine import Document, fields

# Create your models here.
class Url(Document):
    link = fields.StringField()
    uuid = fields.StringField()