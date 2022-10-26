import { Button } from "@mui/material";
import React, { useState } from "react";
import { getRecipeById } from "../../services";
import { DetailedRecipe, Recipe } from "../../utils/types";
import CloseRoundedIcon from "@mui/icons-material/CloseRounded";

interface RecipeCardProps {
  recipe: Recipe;
}

export default function RecipeCard({ recipe }: RecipeCardProps) {
  const [recipeDetails, setRecipeDetails] = useState<DetailedRecipe>(
    {} as DetailedRecipe
  );
  const [displayView, setDisplayView] = useState<boolean>(false);

  const handleViewRecipe = async () => {
    try {
      const details = await getRecipeById(recipe.id);
      setRecipeDetails(details.data);
    } catch (error) {
      console.log(error);
    } finally {
      setDisplayView(true);
    }
  };

  return (
    <div className="flex flex-col w-full border border-blue-300 rounded-md p-2 mt-2">
      <div className="flex flex-row justify-between">
        <span className="text-caption-semibold-1">{recipe.title}</span>
        <span className="text-caption-regular-1">
          {recipe.quantity + " receitas"}
        </span>
      </div>
      <span className="text-caption-regular-1">
        {"Custo médio: R$" + recipe.cost}
      </span>
      <div className="flex flex-row justify-between">
        <span className="text-caption-regular-1">
          {"Preço sugerido: R$" + recipe.revenue}
        </span>
        <Button
          variant="contained"
          style={{
            backgroundColor: "#E0FFF0",
            width: 60,
            color: "#242121",
            textTransform: "none",
            fontFamily: "Montserrat",
            fontWeight: 600,
            fontSize: 10,
          }}
          onClick={handleViewRecipe}
          disableElevation
        >
          Receita
        </Button>
      </div>
      <div
        className={`absolute z-10  px-6 py-4 bg-white rounded-lg max-w-xs shadow-1 ${
          displayView ? "" : "hidden"
        }`}
      >
        <div className="flex flex-col">
            <button className="h-0 " onClick={() => setDisplayView(false)} style={{ flex: 1, alignSelf:'flex-end'}}>
                <CloseRoundedIcon className="text-body-regular-2 text-gray-600" />
            </button>
            <span className="text-caption-semibold-1">{recipe.title}</span>
            <span className="text-caption-regular-1">{recipeDetails.howto}</span>
        </div>
      </div>
    </div>
  );
}
