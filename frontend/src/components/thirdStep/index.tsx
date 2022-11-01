import React from "react";
import { OptimizationResultType } from "../../utils/types";
import RecipeCard from "./RecipeCard";

export interface ThirdStepProps {
  optimizationResult: OptimizationResultType;
  type: string;
}

export default function ThirdStep({
  optimizationResult,
  type,
}: ThirdStepProps) {
  return (
    <section className="flex flex-col w-1/3">
      <h2 className="text-heading-semibold-5 text-blue-100 mb-2">Fim!</h2>
      <div className="flex bg-gray-100 w-11/12 xl:w-3/4 py-10 px-8 rounded-2xl">
        <div className="flex flex-col bg-white shadow-1 rounded-xl w-full py-10 px-8 rounded-2xl">
          <span className="text-body-semibold-1 mb-3">Resultado</span>
          {optimizationResult.recipes.map((item) => {
            if (item.quantity) {
              return <RecipeCard recipe={item} />;
            }
          })}
          <span className="text-caption-semibold-1 mt-4">
            {type === "maxProduction"
              ? "Produção máxima: "
              : type === "maxProfit" ? "Lucro máximo: R$ " : ""}{" "}
            {optimizationResult.Z} {type === "maxProduction" ? " porções" : ""}
          </span>
        </div>
      </div>
    </section>
  );
}
