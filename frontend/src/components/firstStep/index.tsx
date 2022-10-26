import React, { Dispatch, SetStateAction, useState, useCallback, useEffect } from "react";
import {
  Button,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
} from "@mui/material";
import { Ingredient, IngredientListItem } from "../../utils/types";
import { getIngredients } from "../../services";

interface FirstStepProps {
  selectedIngredientsList: IngredientListItem[];
  setSelectedIngredientsList: Dispatch<SetStateAction<IngredientListItem[]>>;
}

export default function FirstStep({
  selectedIngredientsList,
  setSelectedIngredientsList,
}: FirstStepProps) {
  const [ingredientOptions, setIngredientOptions] = useState<Ingredient[]>([])
  const [selectedIngredient, setSelectedIngredient] = useState<Ingredient>();
  const [quantityValue, setQuantityValue] = useState("")

  const findIngredient = (id: string) => ingredientOptions.find((item) =>  item.id === id)

  const clearInputs = () => {
    setSelectedIngredient(undefined)
    setQuantityValue("")
  }

  const clearSelectedIngredientsList = () => setSelectedIngredientsList([])

  const handleIngredientChange = async (event: SelectChangeEvent) => {
    setSelectedIngredient(findIngredient(event.target.value));
  };

  const  handleIngredientOptions = useCallback(async () => {
    const response = await getIngredients()
    setIngredientOptions(response.data.ingredients)
  }, [])

  const handleQuantityInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuantityValue(event.target.value);
  };

  const handleAddIngredient = useCallback(() => {
    if (selectedIngredient) {
      const newIngrendientItem = {
        id: selectedIngredient?.id,
        name: selectedIngredient?.name,
        quantity: quantityValue
      } as IngredientListItem
      setSelectedIngredientsList((prevState) => [...prevState, newIngrendientItem])
      clearInputs()
    }
  }, [selectedIngredient, quantityValue])

  const listSelectedIngredients = () => {
    if(selectedIngredientsList.length > 0 )
      return selectedIngredientsList?.map((item) => {
        const ingredient = findIngredient(item.id)
        return (
          <span id={item.id} key={`${item.id}`} className="text-body-regular-2">
            {ingredient?.name || ""} - {item?.quantity || ""} {ingredient?.unit || ""}
          </span>
        );
      })
    else 
    return (<span className="text-body-regular-2">
      Sua lista está vazia
    </span>)

  }

  useEffect(() => {handleIngredientOptions()}, [])


  return (
    <section className="flex flex-col w-1/3">
      <h2 className="text-heading-semibold-5 text-blue-100 mb-2">Passo 1:</h2>
      <div className="flex flex-col bg-gray-100 w-11/12 xl:w-3/4 py-10 px-8 rounded-2xl">
        <span className="text-body-semibold-1 mb-3">
          Selecione o ingrediente
        </span>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Ex: Leite</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={selectedIngredient?.id || ''}
            label="Ex: Leite"
            onChange={handleIngredientChange}
            style={{ backgroundColor: "white" }}
          >
            {ingredientOptions?.map((ingredient) => <MenuItem value={ingredient.id}>{ingredient.name}</MenuItem>)}
          </Select>
        </FormControl>
        <span className="text-body-semibold-1 my-3">Quantidade em {selectedIngredient?.unit || 'unidade de medida'}</span>
        <TextField
          id="outlined-basic"
          label={`Ex: 12 ${selectedIngredient?.unit || 'u'}`}
          variant="outlined"
          style={{ backgroundColor: "white" }}
          value={quantityValue}
          onChange={handleQuantityInputChange}

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
          onClick={() => handleAddIngredient()}
        >
          Adicionar
        </Button>
      </div>
      <div className="flex flex-col bg-gray-100 w-11/12 xl:w-3/4 py-10 px-8 rounded-2xl mt-5">
        <div className="flex flex-col bg-white shadow-1 rounded-xl max-w-sm py-10 px-8 rounded-2xl">
          <span className="text-body-semibold-1 mb-3">
            Lista de ingredientes adicionados:
          </span>
          {listSelectedIngredients()}
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
          onClick={() => clearSelectedIngredientsList()}
        >
          Limpar
        </Button>
      </div>
    </section>
  );
}
