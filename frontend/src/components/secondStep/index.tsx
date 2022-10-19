import { FormControl, FormControlLabel, FormLabel, Radio, RadioGroup } from "@mui/material";
import React from "react";
import { ReactComponent as TastingImage } from "../../assets/images/tasting.svg";

export default function SecondStep() {
  return (
    <section className="flex flex-col w-1/3">
      <h2 className="text-heading-semibold-5 text-blue-100 mb-2">Passo 2:</h2>
      <div className="flex bg-gray-100 w-3/4 py-10 px-8 rounded-2xl mb-12">
        <div className="flex flex-col bg-white shadow-1 rounded-xl max-w-sm py-10 px-8 rounded-2xl">
          <span className="text-body-semibold-1 mb-3">
            Selecione o método de otimização
          </span>
          <FormControl>
            <RadioGroup
                defaultValue="female"
                name="radio-buttons-group"
            >
                <FormControlLabel value="female" control={<Radio />} label="Maximizar Produção" />
                <FormControlLabel value="male" control={<Radio />} label="Maximizar Lucro" />
            </RadioGroup>
        </FormControl>
        </div>
      </div>
      <div className="flex w-3/4 justify-center">
        <TastingImage />
      </div>
    </section>
  );
}
