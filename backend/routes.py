from flask import Blueprint, request
from . import db, ma
from .models import Recipe, Ingredient, ingredient_schema, many_ingredients_schema




routes = Blueprint("routes", __name__)


@routes.route('/', methods=['GET'])
def home():
    return {"Hello": "World"}

@routes.route('/add-ingredient', methods=['POST'])
def add_ingredient():
    name = request.json['name']
    unit = request.json['unit']

    ingredient = Ingredient(name=name, unit=unit)
    db.session.add(ingredient)
    db.session.commit()
    return ingredient_schema.dump(ingredient)


@routes.route('/show-ingredients', methods=['GET'])
def show_ingredients():
    ingredients = Ingredient.query.all()
    return many_ingredients_schema.dump(ingredients)
