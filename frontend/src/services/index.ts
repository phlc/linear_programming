import axios from 'axios'

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000'
})

export const getIngredients = () => api.get('/show-ingredients')

export const getIngredientByName = (name:string) => {
    const body = {name}
    return api.post('/get-ingredient', body)
}

// /add-ingredient