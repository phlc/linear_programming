from flask import Blueprint, request
from . import db, ma
from .models import Recipe, Ingredient, ingredient_schema, many_ingredients_schema
from .models import recipe_schema, many_recipes_schema, validate_ingredients, add_new_recipe
from .optimization import load_model, optimize


routes = Blueprint("routes", __name__) # Blueprint object


@routes.route('/', methods=['GET'])
def home():
    """ Root route - used only for tests """
    return {"Hello": "World"}


@routes.route('/show-ingredients', methods=['GET'])
def show_ingredients():
    """ /show-ingredients route - show all ingredients in the database """
    ingredients = Ingredient.query.all()
    return {"ingredients": many_ingredients_schema.dump(ingredients)}

@routes.route('/get-ingredient', methods=['POST'])
def get_ingredient():
    """ /get-ingredient route - gets one ingredient based on name """
    name = request.json['name'].lower()
    ingredient = Ingredient.query.filter_by(name=name).first()
    if(ingredient == None):
        return {'error': 'Ingredient not Found', 'type': 1}
    return ingredient_schema.dump(ingredient)

@routes.route('/add-ingredient', methods=['POST'])
def add_ingredient():
    """ /add-ingredient route - add one ingredient to the database """
    name = None
    unit = None
    try:
        name = request.json['name']
        unit = request.json['unit']
    except:
        pass
    
    # check if json is correct 
    if(name == None or unit == None):
        return {'error': 'name or unit missing', 'type': 2}
    if(Ingredient.query.filter_by(name=name).first() != None):
        return {'error': 'ingredient already exists', 'type': 3}

    # create and add ingredient to database
    ingredient = Ingredient(name=name.lower(), unit=unit.lower())
    db.session.add(ingredient)
    db.session.commit()
    load_model()
    return ingredient_schema.dump(ingredient)


@routes.route('/show-recipes', methods=['GET'])
def show_recipes():
    """ /show-recipes route - show all recipes in the database """
    recipes = Recipe.query.all()
    return {"recipes": many_recipes_schema.dump(recipes)}

@routes.route('/get-recipe', methods=['POST'])
def get_recipe():
    """ /get-recipe route - gets one recipe based on id """
    id = request.json['id']
    recipe = Recipe.query.get(id)
    if(recipe == None):
        return {'error': 'Recipe not Found', 'type': 4}
    return recipe_schema.dump(recipe)

@routes.route('/add-recipe', methods=['POST'])
def add_recipe():
    """ /add-recipe route - adds one recipe to the database """
    recipe = add_new_recipe(request.json)
    if(not recipe['valid']):
        return {'errors': recipe['errors']}
    load_model()
    return recipe['object']


@routes.route('/optimize-production', methods=['POST'])
def optimize_production():
    """ /optimize-produciton route - Find the optimal production based on inventory ingredients """

    inventory = validate_ingredients(request.json) # check if json data is correct
    if(inventory['valid']):
        return optimize(objective='production', inventory=inventory['list'])
    return {'errors': inventory['errors']}



@routes.route('/optimize-profit', methods=['POST'])
def optimize_profit():
    """ /optimize-profit route - Find the optimal profit based on inventory ingredients """

    inventory = validate_ingredients(request.json) # check if json data is correct
    if(inventory['valid']):
        return optimize(objective='profit', inventory=inventory['list'])
    return {'errors': inventory['errors']}