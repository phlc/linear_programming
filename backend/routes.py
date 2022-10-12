from flask import Blueprint, request
from . import db, ma
from .models import Recipe, Ingredient, ingredient_schema, many_ingredients_schema
from .models import recipe_schema, many_recipes_schema, validate_ingredients, validate_recipe




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
        return {'error': 'Ingredient not Found', 'type': 1}
    return ingredient_schema.dump(ingredient)

@routes.route('/add-ingredient', methods=['POST'])
def add_ingredient():
    name = request.json['name'].lower()
    unit = request.json['unit'].lower()

    if(name == None or unit == None):
        return {'error': 'name or unit missing', 'type': 2}
    if(Ingredient.query.filter_by(name=name).first() != None):
        return {'error': 'ingredient already exists', 'type': 3}

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
        return {'error': 'Recipe not Found', 'type': 4}
    return recipe_schema.dump(recipe)

@routes.route('/add-recipe', methods=['POST'])
def add_recipe():
    recipe = validate_recipe(request.json)
    if(not recipe['valid']):
        return {'errors': recipe['errors']}
    return recipe['object']


@routes.route('/optimize-production', methods=['POST'])
def optimize_production():
    inventory = validate_ingredients(request.json)
    return inventory


@routes.route('/optimize-profit', methods=['POST'])
def optimize_profit():
    inventory = validate_ingredients(request.json)
    return inventory