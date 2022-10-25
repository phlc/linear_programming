import { Button, FormControl, FormControlLabel, Radio, RadioGroup } from "@mui/material";
import React, {Dispatch, SetStateAction, useState} from "react";
import { ReactComponent as TastingImage } from "../../assets/images/tasting.svg";
import { getOtimizationResult } from "../../services";
import { IngredientListItem, OtimizationResultType } from "../../utils/types";

export interface SecondStepProps {
  selectedIngredientsList: IngredientListItem[];
  setOtimizationResult: Dispatch<SetStateAction<OtimizationResultType>>;
}

export default function SecondStep({selectedIngredientsList, setOtimizationResult}: SecondStepProps) {
  const [objective, setObjective] = useState("maxProdution")

  const handleOnSubmit = async () => {
    try {
      const ingredients = selectedIngredientsList.map((ingredient) => ({name: ingredient.name, quantity: ingredient.quantity}))
      const response = await getOtimizationResult(objective,ingredients)

      setOtimizationResult(response.data)

    } catch (erro) {
      console.log("Error", erro)
    }
  }

  return (
    <section className="flex flex-col w-1/3">
      <h2 className="text-heading-semibold-5 text-blue-100 mb-2">Passo 2:</h2>
      <div className="flex flex-col bg-gray-100 w-3/4 py-10 px-8 rounded-2xl mb-12">
        <div className="flex flex-col bg-white shadow-1 rounded-xl max-w-sm py-10 px-8 rounded-2xl">
          <span className="text-body-semibold-1 mb-3">
            Selecione o método de otimização
          </span>
          <FormControl>
            <RadioGroup
                defaultValue="maxProdution"
                name="radio-buttons-group"
                onChange={(e) => setObjective(e.target.value)}
            >
                <FormControlLabel value="maxProdution" control={<Radio />} label="Maximizar Produção" />
                <FormControlLabel value="maxProfit" control={<Radio />} label="Maximizar Lucro" />
            </RadioGroup>
        </FormControl>
        </div>
        <Button
          variant="contained"
          style={{
            backgroundColor: "#E0FFF0",
            width: 107,
            alignSelf: "flex-end",
            color: "#242121",
            textTransform: "none",
            fontFamily: "Montserrat",
            fontWeight: 600,
            marginTop: 20,
          }}
          onClick={handleOnSubmit}
        >
          Calcular
        </Button>
      </div>
      <div className="flex w-3/4 justify-center">
        <TastingImage />
      </div>
    </section>
  );
}
