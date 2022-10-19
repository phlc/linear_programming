import { FormControl, InputLabel, MenuItem, Select, SelectChangeEvent } from '@mui/material';
import React, { useState } from 'react';

export default function LandingPage () {
    const [age, setAge] = useState('');
    const handleChange = (event: SelectChangeEvent) => {
        setAge(event.target.value);
      };

    return (
        <div className="flex bg-blue-200 min-h-screen p-12" >
            <div className="flex flex-col bg-white shadow-1 rounded-3xl min-w-full p-6">
                <h1 className="text-heading-semibold-4 mb-6">Otimização de Alimentos</h1>
                <div className="flex flex-row min-w-full  justify-between">
                    <section className='flex flex-col w-96'>
                        <h2 className="text-heading-semibold-5 text-blue-100">Passo 1:</h2>
                        <div className='flex flex-col bg-gray-100 max-w-sm py-10 px-8 max-h-72 rounded-2xl'>
                            <span className='text-body-bold-1 mb-4'>Selecione o ingrediente</span>
                            <FormControl fullWidth>
                                <InputLabel id="demo-simple-select-label">Ex: Leite</InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    value={age}
                                    label="Ex: Leite"
                                    onChange={handleChange}
                                >
                                    <MenuItem value={10}>Ten</MenuItem>
                                    <MenuItem value={20}>Twenty</MenuItem>
                                    <MenuItem value={30}>Thirty</MenuItem>
                                </Select>
                            </FormControl>
                        </div>
                    </section>
                    <section className='flex flex-col'>
                        <h2 className="text-heading-semibold-5 text-blue-100">Passo 2:</h2>
                        <div className='flex bg-gray-100 max-w-sm py-10 px-8 max-h-72 rounded-2xl'>
                            
                        </div>
                    </section>
                    <section className='flex flex-col'>
                        <h2 className="text-heading-semibold-5 text-blue-100">Fim!</h2>
                        <div className='flex bg-gray-100 max-w-sm py-10 px-8 max-h-72 rounded-2xl'>
                            
                        </div>
                    </section>
                </div>
            </div>
        </div>
     )
};