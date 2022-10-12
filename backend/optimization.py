from pulp import *
from sqlalchemy import func
from . import db
from .models import Recipe, Ingredient

recipes_ingredients=None
portions=None
cost=None
revenue=None
model_loaded = False

def load_model():
    global recipes_ingredients
    global portions
    global cost
    global revenue
    global model_loaded

    max_id_recipe = db.session.query(func.max(Recipe.id)).scalar() + 1
    max_id_ingredient = db.session.query(func.max(Ingredient.id)).scalar() + 1

    recipes_ingredients = []
    for i in range(max_id_recipe):
        recipes_ingredients.append([0]*max_id_ingredient)
    portions = [0]*max_id_recipe
    cost = [0]*max_id_recipe
    revenue = [0]*max_id_recipe

    recipes = Recipe.query.all()

    for recipe in recipes:
        portions[recipe.id] = recipe.portions
        cost[recipe.id] = recipe.cost
        revenue[recipe.id] = recipe.revenue

        for ingredient in recipe.ingredients:
            print(ingredient.recipe_id, ingredient.ingredient_id, ingredient.quantity)
            recipes_ingredients[ingredient.recipe_id][ingredient.ingredient_id] = ingredient.quantity

    print(recipes_ingredients)
    print(portions)
    print(cost)
    print(revenue)
    model_loaded = True




def optimize(objective='production', inventory=None):
    global recipes_ingredients
    global portions
    global cost
    global revenue
    global model_loaded
    solution = {"recipes": [], "Z": 0}

    if(not model_loaded):
        load_model()
    
    prob = None
    obj_func = None
    variables = [LpVariable(f"{i}", 0, None, LpInteger) for i in range(len(portions))]

    if(objective == 'production'):
        prob = LpProblem("Maximize Production", LpMaximize)
        obj_func = sum(p * v for p,v in zip(portions, variables))
    elif(objective == 'profit'):
        prob = LpProblem("Maximize Profit", LpMaximize)
        obj_func = sum((r * v  -  c * v) for r,c,v in zip(revenue, cost, variables))

    prob += obj_func, "Max Z"

    for i in range(len(inventory)):
        restriction = sum(recipes_ingredients[j][i] * variables[j] for j in range(len(variables)))
        prob += restriction <= inventory[i]

    prob.solve()
    for v in prob.variables():
        solution["recipes"].append({f"{v.name}": v.varValue})
   
    solution["Z"] = value(prob.objective)

    return solution

