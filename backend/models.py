from . import db, ma

# Tables
class Association(db.Model):
    __tablename__ = "association"
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column('recipe_id', db.Integer, db.ForeignKey("recipe.id"))
    ingredient_id = db.Column('ingredient_id', db.Integer, db.ForeignKey("ingredient.id"))
    quantity = db.Column(db.Integer)
    ingredient = db.relationship("Ingredient", back_populates="recipes")
    recipe = db.relationship("Recipe", back_populates="ingredients")

class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    howto = db.Column(db.Text)
    portions = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    revenue = db.Column(db.Integer)
    ingredients = db.relationship('Association', back_populates='recipe')

class Ingredient(db.Model):
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    unit = db.Column(db.String(10))
    recipes = db.relationship('Association', back_populates='ingredient')

# Schemas
class IngredientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'unit')
        ordered = True

ingredient_schema = IngredientSchema()
many_ingredients_schema = IngredientSchema(many=True)

class AssociationSchema(ma.Schema):
    ingredient = ma.Nested(IngredientSchema)

    class Meta:
        fields = ('id', 'ingredient', 'quantity')
        ordered = True

class RecipeSchema(ma.Schema):
    ingredients = ma.Nested(AssociationSchema, many=True)

    class Meta:
        fields = ('cost', 'id', 'ingredients', 'howto', 'portions', 'revenue', 'title')
        ordered = True

recipe_schema = RecipeSchema()
many_recipes_schema = RecipeSchema(many=True)

# Helpers

def validate_recipe(data):
    response = {'valid': True, 'errors': [], 'object': None}
    title = data['title']
    howto = data['howto']
    portions = data['portions']
    cost = data['cost']
    revenue = data['revenue']
    ingredients = data['ingredients']
    ids = []

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
                response['errors'].append({{'ingredients': f"{ingredient['name']} without quantity"}})
                response['valid'] = False
            if(response['valid']):
                ids.append((ingredient_id.id, ingredient['quantity']))
    
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
    ingredients = data['ingredients']
    response = {'valid': True, 'errors': [], 'object': None}
    ids = []
    if(ingredients == None or len(ingredients)<1):
        response['errors'].append({'ingredients': 'not found'})
        response['valid'] = False
    else:
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
                ids.append((ingredient_id.id, ingredient['quantity']))
        response['object'] = ids
    return response