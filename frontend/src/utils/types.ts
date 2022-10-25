export interface Ingredient {
    id: string
    name: string
    unit: string
}

export interface Recipe {
    id: string
    name?: string
    quantity: string
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