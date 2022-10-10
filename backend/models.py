from enum import unique
from . import db 
from sqlalchemy.sql import func


recipe_ingredient = db.Table('recipe_ingredient',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
)



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    prepare = db.Column(db.Text)
    ingredients = db.relationship('Ingredient', secondary=recipe_ingredient, backref='ingredients')

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    unit = db.Column(db.String(10))
