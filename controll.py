from PIL import Image
from models import *
import random


CATEGORY_CLASS = [
    "bg-primary",
    "bg-secondary",
    "bg-success",
    "bg-danger",
    "bg-warning",
    "bg-info",
    "bg-light",
    "bg-dark"
]

CATEGORY_COLOR_TEXT = [
    "bg-warning",
    "bg-info",
    "bg-light"
]


def sort_articles(iterable):
    data = []
    data_result = []
    for i in iterable:
        if len(data_result) == 3:
            data.append(data_result)
            data_result = []
        data_result.append(i)
    if data_result: data.append(data_result)
    return data


def get_data_for_index_page(page=None):
    try:
        if page is None: page = 1
        data = Content.select().paginate(page=page, paginate_by=9)
        if len(data) > 3:
            data = sort_articles(data)
        else:
            return [data]
        return data
    except Exception as e:
        print(e)
        return None


def get_article(slug):
    try:
        article = Content.get_or_none(Content.slug == slug.strip())
        return article
    except Exception as e:
        print(e)
        return None


def get_data_for_category_page(slug):
    try:
        category_id = Category.get_or_none(Category.slug == slug).id
        data = Content.select().where(Content.category == category_id)
        if len(data) > 3:
            data = sort_articles(data)
        else:
            return [data]
        return data
    except Exception as e:
        print(e)
        return None


def get_category():
    data_class = []
    category = Category.select()
    for c in range(len(category)):
        data_class.append(CATEGORY_CLASS[random.randint(0, len(CATEGORY_CLASS) -1 )])
    return [category, data_class, CATEGORY_COLOR_TEXT, len(category)]
