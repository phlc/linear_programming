from . import db 
from sqlalchemy.sql import func



class Association(db.Model):
    __tablename__ = "association"
    left_id = db.Column(db.ForeignKey("left.id"), primary_key=True)
    right_id = db.Column(db.ForeignKey("right.id"), primary_key=True)
    quantity = db.Column('quantity', db.Integer)
    ingredient = db.relationship("Ingredient", back_populates="recipes")
    recipe = db.relationship("Recipe", back_populates="ingredients")


class Recipe(db.Model):
    __tablename__ = "left"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    howto = db.Column(db.Text)
    ingredients = db.relationship('Association', back_populates='recipes')

class Ingredient(db.Model):
    __tablename__ = "right"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    unit = db.Column(db.String(20))
    recipes = db.relationship('Association', back_populates='ingredients')

