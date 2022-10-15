# Sets
set Recipes;
set Ingredients;

# Parameters
param q{i in Recipes}; 						# quantity produced by 1 recipe i
param v{i in Recipes}; 						# revenue from 1 recipe i
param c{i in Recipes}; 						# cost of 1 recipe i
param g{i in Recipes, j in Ingredients}; 	# quantity of ingredient j needed for recipe i
param e{j in Ingredients};					# quantity of ingredient j in inventory

# Decision Variable
var r{i in Recipes} integer >= 0;						# quantity of recipe i to be prepared

# Objectives
# Maximize Production
maximize Z1: sum{i in Recipes} r[i] * q[i];
	
# Maximize Profit
# maximize Z2: sum{i in Recipes} r[i] * (v[i] - c[i]);
	
	
# Restrictions
	
# Ingredients in Inventory
subject to max_inventory{j in Ingredients}: sum{i in Recipes} r[i]*g[i,j] <= e[j];

#Não Negatividade
subject to nao_neg{i in Recipes, j in Ingredients}: g[i,j] >= 0;
	
	 
	