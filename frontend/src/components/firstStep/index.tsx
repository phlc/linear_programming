import React, { Dispatch, SetStateAction } from "react";
import {
  Button,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
} from "@mui/material";

interface FirstStepProps {
  ingredient: string;
  handleIngredientChange: (event: SelectChangeEvent) => void;
  setIngredientsList: Dispatch<SetStateAction<string[]>>;
  ingredientsList: string[];
}

export default function FirstStep({
  ingredient,
  handleIngredientChange,
  ingredientsList,
  setIngredientsList,
}: FirstStepProps) {
  return (
    <section className="flex flex-col w-1/3">
      <h2 className="text-heading-semibold-5 text-blue-100 mb-2">Passo 1:</h2>
      <div className="flex flex-col bg-gray-100 w-3/4 py-10 px-8 rounded-2xl">
        <span className="text-body-semibold-1 mb-3">
          Selecione o ingrediente
        </span>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Ex: Leite</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={ingredient}
            label="Ex: Leite"
            onChange={handleIngredientChange}
            style={{ backgroundColor: "white" }}
          >
            <MenuItem value={10}>Ten</MenuItem>
            <MenuItem value={20}>Twenty</MenuItem>
            <MenuItem value={30}>Thirty</MenuItem>
          </Select>
        </FormControl>
        <span className="text-body-semibold-1 my-3">Quantidade</span>
        <TextField
          id="outlined-basic"
          label="Ex: 12L"
          variant="outlined"
          style={{ backgroundColor: "white" }}
        />
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
        >
          Adicionar
        </Button>
      </div>
      <div className="flex flex-col bg-gray-100 w-3/4 py-10 px-8 rounded-2xl mt-5">
        <div className="flex flex-col bg-white shadow-1 rounded-xl max-w-sm py-10 px-8 rounded-2xl">
          <span className="text-body-semibold-1 mb-3">
            Lista de ingredientes adicionados:
          </span>
          {ingredientsList.map((item) => {
            return (
              <span id={item} key={`${item}`} className="text-body-regular-2">
                {item}
              </span>
            );
          })}
        </div>
        <Button
          variant="contained"
          style={{
            backgroundColor: "#FFE0E0",
            width: 107,
            alignSelf: "flex-end",
            color: "#242121",
            textTransform: "none",
            fontFamily: "Montserrat",
            fontWeight: 600,
            marginTop: 20,
          }}
        >
          Limpar
        </Button>
      </div>
    </section>
  );
}
