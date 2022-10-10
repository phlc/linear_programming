from enum import unique
from . import db 
from sqlalchemy.sql import func



class Association(db.Model):
    __tablename__ = "association"
    recipe_id = db.Column(db.ForeignKey("recipe.id"), primary_key=True)
    ingredient_id = db.Column(db.ForeignKey("ingredient.id"), primary_key=True)
    quantity = db.Column(db.Integer)
    ingredient = db.relationship("Ingredient", back_populates="recipes")
    recipe = db.relationship("Recipe", back_populates="ingredients")



class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    prepare = db.Column(db.Text)
    ingredients = db.relationship('Association', back_populates='recipes')

class Ingredient(db.Model):
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    unit = db.Column(db.String(10))
    recipes = db.relationship('Association', back_populates='ingredients')
