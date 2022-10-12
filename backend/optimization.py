from pulp import *

def optimize(objective='production', recipes_ingredients=None, portions=None, cost=None, revenue=None, inventory=None):
    
    prob = None
    obj_func = None
    variables = [LpVariable(f"{i+1}", 0, None, LpInteger) for i in range(len(recipes_ingredients))]

    if(objective == 'production'):
        prob = LpProblem("Maximize Production", LpMaximize)
        obj_func = sum(p * v for p,v in zip(portions, variables))
    elif(objective == 'profit'):
        prob = LpProblem("Maximize Profit", LpMaximize)
        obj_func = sum((r * v  -  c * v) for r,c,v in zip(revenue, cost, variables))

    prob += obj_func, "Max Z"

    for i in range(len(inventory)):
        restriction = sum(r * v for r,v in zip(recipes_ingredients[i], variables))
        prob += restriction <= inventory[i]

    prob.solve()
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Z = ", value(prob.objective))
