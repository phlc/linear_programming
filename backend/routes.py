from flask import Blueprint, request
from . import db, ma
from .models import Recipe, Ingredient, ingredient_schema, many_ingredients_schema, recipe_schema, many_recipes_schema




routes = Blueprint("routes", __name__)


@routes.route('/', methods=['GET'])
def home():
    return {"Hello": "World"}


@routes.route('/show-ingredients', methods=['GET'])
def show_ingredients():
    ingredients = Ingredient.query.all()
    return many_ingredients_schema.dump(ingredients)

@routes.route('/get-ingredient', methods=['POST'])
def get_ingredient():
    name = request.json['name'].lower()
    ingredient = Ingredient.query.filter_by(name=name).first()
    if(ingredient == None):
        return {'Error': 'Ingredient not Found'}
    return ingredient_schema.dump(ingredient)

@routes.route('/add-ingredient', methods=['POST'])
def add_ingredient():
    name = request.json['name'].lower()
    unit = request.json['unit'].lower()

    ingredient = Ingredient(name=name, unit=unit)
    db.session.add(ingredient)
    db.session.commit()
    return ingredient_schema.dump(ingredient)


@routes.route('/show-recipes', methods=['GET'])
def show_recipes():
    recipes = Recipe.query.all()
    return many_recipes_schema.dump(recipes)

@routes.route('/get-recipe', methods=['POST'])
def get_recipe():
    id = request.json['id']
    recipe = Recipe.query.get(id)
    if(recipe == None):
        return {'Error': 'Recipe not Found'}
    return recipe_schema.dump(recipe)

@routes.route('/add-recipe', methods=['POST'])
def add_recipe():
    