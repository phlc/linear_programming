import axios from 'axios'

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000'
})

export const getIngredients = () => api.get('/show-ingredients')

export const getIngredientByName = (name:string) => {
    const body = {name}
    return api.post('/get-ingredient', body)
}

export const getOptimizationResult = (objective: string, ingredients: {name: string, quantity: number}[]  ) => {
    const body = {ingredients}
    console.log(JSON.stringify(body))
    if(objective === 'maxProduction')
        return api.post('/optimize-production', body)
    else 
        return api.post('/optimize-profit', body)
}

export const getRecipeById = (id: string) => {
    const body = {id}
   
    return api.post('/get-recipe', body)
}