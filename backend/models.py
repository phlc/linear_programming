from . import db, ma
from sqlalchemy import func

# Tables
class Association(db.Model):
    """ Many to Many Association Table between Recipe and Ingredient plus extra field (quantity)"""
    __tablename__ = "association"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column('recipe_id', db.Integer, db.ForeignKey("recipe.id"))
    ingredient_id = db.Column('ingredient_id', db.Integer, db.ForeignKey("ingredient.id"))
    quantity = db.Column(db.Integer)

    # Relations
    ingredient = db.relationship("Ingredient", back_populates="recipes")
    recipe = db.relationship("Recipe", back_populates="ingredients")

class Recipe(db.Model):
    """ Class for recipes and creation of the database recipe table """
    __tablename__ = "recipe"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    howto = db.Column(db.Text)
    portions = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    revenue = db.Column(db.Integer)

    # Relation
    ingredients = db.relationship('Association', back_populates='recipe')

class Ingredient(db.Model):
    """ Class for ingredient and creation of the database ingredient table """
    __tablename__ = "ingredient"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    unit = db.Column(db.String(10))

    # Relation
    recipes = db.relationship('Association', back_populates='ingredient')

# Schemas
class IngredientSchema(ma.Schema):
    """Marshmallow schema for Ingredient class"""
    class Meta:
        fields = ('id', 'name', 'unit')
        ordered = True

# Schema instances
ingredient_schema = IngredientSchema()                  # one ingredient
many_ingredients_schema = IngredientSchema(many=True)   # many ingrediets

class AssociationSchema(ma.Schema):
    """Marshmallow schema for Association class"""
    ingredient = ma.Nested(IngredientSchema)

    class Meta:
        fields = ('id', 'ingredient', 'quantity')
        ordered = True

class RecipeSchema(ma.Schema):
    """Marshmallow schema for Recipe class"""
    ingredients = ma.Nested(AssociationSchema, many=True)

    class Meta:
        fields = ('cost', 'id', 'ingredients', 'howto', 'portions', 'revenue', 'title')
        ordered = True

# Schema instaces
recipe_schema = RecipeSchema()                  # one recipe
many_recipes_schema = RecipeSchema(many=True)   # many recipes



# Helper Methods
def add_new_recipe(data):
    """ Adds new recipe

        First checks if all json fields are correct 
        if not: returns json with 'valid': false, and 'errors' log
        if correct: returns json whit new recipe schema - 'object'
    """
    response = {'valid': True, 'errors': [], 'object': None}
    title = data['title']
    howto = data['howto']
    portions = data['portions']
    cost = data['cost']
    revenue = data['revenue']
    ingredients = data['ingredients']
    ids = []

    # Check Recipe Fields
    if(title == None):
        response['errors'].append({'title': 'not found'})
        response['valid'] = False
    if(Recipe.query.filter_by(title=title).first() != None):
        response['errors'].append({'title': 'already exists'})
        response['valid'] = False
    if(howto == None):
        response['errors'].append({'howto': 'not found'})
        response['valid'] = False
    if(portions == None):
        response['errors'].append({'portions': 'not found'})
        response['valid'] = False
    if(cost == None):
        response['errors'].append({'cost': 'not found'})
        response['valid'] = False
    if(revenue == None):
        response['errors'].append({'revenue': 'not found'})
        response['valid'] = False
    
    if(ingredients == None or len(ingredients)<1):
        response['errors'].append({'ingredients': 'not found'})
        response['valid'] = False
    else:
        # Check each ingredient
        for ingredient in ingredients:
            ingredient_id = None
            if(ingredient['name'] == None):
                response['errors'].append({'ingredient': 'without name'})
                response['valid'] = False
            else:
                # check if ingredient is in the database
                ingredient_id = Ingredient.query.filter_by(name=ingredient['name']).first()
            if(ingredient_id == None):
                response['errors'].append({'ingredients': f"{ingredient['name']} not found in database"})
                response['valid'] = False

            if(ingredient['quantity'] == None):
                response['errors'].append({{'ingredients': f"{ingredient['name']} without quantity"}})
                response['valid'] = False
            if(response['valid']):
                ids.append((ingredient_id.id, ingredient['quantity']))
    
    # Create recipe and add to database
    if(response['valid']):
        recipe = Recipe(title=title, howto=howto, portions=portions, cost=cost, revenue=revenue)
        db.session.add(recipe)
        db.session.commit()
        for id in ids:
            db.session.add(Association(recipe_id=recipe.id, ingredient_id=id[0], quantity=id[1]))
        db.session.commit()
        response['object'] = recipe_schema.dump(recipe)

    return response


def validate_ingredients(data):
    """ Validates and Creates a list of ingredients IDs """
    ingredients = data['ingredients']
    response = {'valid': True, 'errors': [], 'list': None}

    # list of ingredients indexed by ids
    ids = [0] * (db.session.query(func.max(Ingredient.id)).scalar() + 1)

    # Check if json data is correct
    if(ingredients == None or len(ingredients)<1):
        response['errors'].append({'ingredients': 'not found'})
        response['valid'] = False
    else:
        # Check each ingredient
        for ingredient in ingredients:
            ingredient_id = None
            if(ingredient['name'] == None):
                response['errors'].append({'ingredient': 'without name'})
                response['valid'] = False
            else:
                ingredient_id = Ingredient.query.filter_by(name=ingredient['name']).first()
            if(ingredient_id == None):
                response['errors'].append({'ingredients': f"{ingredient['name']} not found in database"})
                response['valid'] = False
            if(ingredient['quantity'] == None):
                response['errors'].append({'ingredients': f"{ingredient['name']} without quantity"})
                response['valid'] = False
            if(response['valid']):
                ids[ingredient_id.id] = ingredient['quantity']
        response['list'] = ids

    return response