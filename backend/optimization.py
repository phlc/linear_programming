from pulp import *
from sqlalchemy import func
from . import db
from .models import Recipe, Ingredient

# Global Variables
recipes_ingredients=None
portions=None
cost=None
revenue=None
model_loaded = False

def load_model():
    """ Loads model data from database 
    
        Loads model if not loaded or new recipe or ingredient was created after last load
        To reduce number of database access recipes and ingredients necessary data are 
        store at global variables
    """
    global recipes_ingredients
    global portions
    global cost
    global revenue
    global model_loaded

    # recipes_ingredients, portions, cost and revenue lists are indexed by ids
    max_id_recipe = db.session.query(func.max(Recipe.id)).scalar() + 1
    max_id_ingredient = db.session.query(func.max(Ingredient.id)).scalar() + 1

    # 2D list index by [recipe_id][ingredient_id]
    recipes_ingredients = []
    for i in range(max_id_recipe):
        recipes_ingredients.append([0]*max_id_ingredient)

    # Lists indexed by recipe_id
    portions = [0]*max_id_recipe
    cost = [0]*max_id_recipe
    revenue = [0]*max_id_recipe

    # Load all recipes
    recipes = Recipe.query.all()

    # Load recipes data
    for recipe in recipes:
        portions[recipe.id] = recipe.portions
        cost[recipe.id] = recipe.cost
        revenue[recipe.id] = recipe.revenue

        # Load ingredients data
        for ingredient in recipe.ingredients:
            recipes_ingredients[ingredient.recipe_id][ingredient.ingredient_id] = ingredient.quantity

    model_loaded = True




def optimize(objective='production', inventory=None):
    """ Find the optimal production or profit recipes based on inventory ingredients """
    global recipes_ingredients
    global portions
    global cost
    global revenue
    global model_loaded

    solution = {"recipes": [], "Z": 0} # Solution Dictionary

    if(not model_loaded):
        load_model()
    

    # Pulps model 
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

    # Load dictionary with solution's data
    for v in prob.variables():
        recipe = Recipe.query.get(int(v.name))
        solution["recipes"].append({"id": int(v.name), 
                                    "quantity": v.varValue, 
                                    "title": recipe.title,
                                    "cost": recipe.cost,
                                    "revenue": recipe.revenue,
                                    "portions": recipe.portions}
                                  )
   
    solution["Z"] = value(prob.objective)

    return solution

