import React from 'react';
import { Recipe } from '../../utils/types';

interface RecipeCardProps {
    recipe: Recipe;
}

export default function RecipeCard ({
    recipe
}: RecipeCardProps) {
    return (
        <div className='flex flex-col w-full border-blue-300 rounded-md'>
            {recipe.name}
        </div>
    );
}