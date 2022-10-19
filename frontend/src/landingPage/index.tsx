import {
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
} from "@mui/material";
import React, { useState } from "react";
import FirstStep from "../components/firstStep/firstStep";

export default function LandingPage() {
  const [ingredient, setIngredient] = useState("");
  const [ingredientsList, setIngredientsList] = useState([]);

  const handleIngredientChange = (event: SelectChangeEvent) => {
    setIngredient(event.target.value);
  };

  return (
    <div className="flex bg-blue-200 min-h-screen p-12">
      <div className="flex flex-col bg-white shadow-1 rounded-3xl min-w-full p-10">
        <h1 className="text-heading-semibold-4 mb-6">
          Otimização de Alimentos
        </h1>
        <div className="flex flex-row min-w-full  justify-between">
          <FirstStep
            ingredient={ingredient}
            handleIngredientChange={handleIngredientChange}
            ingredientsList={ingredientsList}
            setIngredientsList={setIngredientsList}
          />
          <section className="flex flex-col w-1/3">
            <h2 className="text-heading-semibold-5 text-blue-100 mb-2">
              Passo 2:
            </h2>
            <div className="flex bg-gray-100 max-w-sm py-10 px-8 max-h-72 rounded-2xl"></div>
          </section>
          <section className="flex flex-col w-1/3">
            <h2 className="text-heading-semibold-5 text-blue-100 mb-2">Fim!</h2>
            <div className="flex bg-gray-100 max-w-sm py-10 px-8 max-h-72 rounded-2xl"></div>
          </section>
        </div>
      </div>
    </div>
  );
}
