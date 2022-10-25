import {
  SelectChangeEvent
} from "@mui/material";
import React, { useState } from "react";
import FirstStep from "../components/firstStep";
import SecondStep from "../components/secondStep";
import ThirdStep from "../components/thirdStep";
import { IngredientListItem, OtimizationResultType } from "../utils/types";

export default function LandingPage() {
  
  const [selectedIngredientsList, setSelectedIngredientsList] = useState<IngredientListItem[]>([]);
  const [otimizationResult, setOtimizationResult] = useState<OtimizationResultType> ({Z: '', recipes: []})
  return (
    <div className="flex bg-blue-200 min-h-screen p-12">
      <div className="flex flex-col bg-white shadow-1 rounded-3xl min-w-full p-10">
        <h1 className="text-heading-semibold-4 mb-6">
          Otimização de Alimentos
        </h1>
        <div className="flex flex-row min-w-full  justify-between">
          <FirstStep
            setSelectedIngredientsList={setSelectedIngredientsList}
            selectedIngredientsList={selectedIngredientsList}
          />
          <SecondStep 
            selectedIngredientsList={selectedIngredientsList} 
            setOtimizationResult={setOtimizationResult} 
          />
          <ThirdStep otimizationResult={otimizationResult}/>
        </div>
      </div>
    </div>
  );
}
