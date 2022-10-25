export interface Ingredient {
    id: string
    name: string
    unit: string
}

export interface IngredientRecipe {
    id: string
    quantity: string
    ingredient: Ingredient
}

export interface Recipe {
    id: string
    name?: string
    quantity: string
}

export interface DetailedRecipe {
    id: string
    title: string
    cost: string
    howto: string
    ingredients: IngredientRecipe[]
    portions: string
    revenue: string
}

export interface IngredientListItem {
    id: string
    name: string
    quantity: string
}

export interface OtimizationResultType {
    Z: string
    recipes: Recipe[]
}