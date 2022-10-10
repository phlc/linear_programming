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

ingredient_schema = IngredientSchema()
many_ingredients_schema = IngredientSchema(many=True)
