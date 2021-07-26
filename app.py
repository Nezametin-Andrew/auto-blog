from flask import Flask, render_template, request, url_for, Markup
from models import Category
import config
import controll as con


app = Flask(__name__)
app.config.from_object(config.Configuration)


@app.route("/")
def index():
    data = con.get_data_for_index_page()
    category = con.get_category()
    return render_template("index.html", data=data, category=category)


@app.route("/blog/<slug>")
def blog_material(slug):
    article = con.get_article(slug)
    category = con.get_category()
    return render_template("article.html", data=article, category=category)


@app.route("/category/<slug>")
def category_page(slug):
    from models import Category
    category_name = Category.get_or_none(Category.slug == slug).name
    data = con.get_data_for_category_page(slug)
    category = con.get_category()
    return render_template("category.html", data=data, category=category, category_name=category_name)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")