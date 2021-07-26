import datetime
from peewee import *
from PIL import Image


db = SqliteDatabase("data.db")


class BaseModel(Model):

    class Meta:
        database = db


class Category(BaseModel):

    name = TextField(verbose_name="")
    slug = TextField(unique=True, verbose_name="")


class Author(BaseModel):

    name = TextField(unique=True, verbose_name="")


class Content(BaseModel):

    title = TextField(unique=True, verbose_name="")
    content = TextField(unique=True, verbose_name="")
    category = ForeignKeyField(Category, field="id", null=True)
    slug = TextField(unique=True, verbose_name="")
    img = TextField()
    author = ForeignKeyField(Author, field="id", null=True)
    created_at = DateTimeField(default=datetime.datetime.now, verbose_name="")
    is_published = BooleanField(default=False, verbose_name="")

    def get_category(self):
        if self.category:
            return Category.get_or_none(Category.id == self.category).name
        return None

    def get_author(self):
        if self.author:
            return Author.get_or_none(Author.id == self.author).name
        return None

    def get_slug_for_url(self):
        url_slug = Category.get_or_none(Category.id == self.category).slug
        return url_slug
