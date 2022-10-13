### Backend

Python based API to find optimal combination of recipes based on inventory's ingredients

    # Usage:

        python main.py


    # Routes:

        /show-ingredients - shows all ingredients in the database
            # Request Method:
                GET

            # response:
                JSON
                Example:
                    {
                        "ingredients": [
                            {
                                "id": 1,
                                "name": "açúcar",
                                "unit": "colheres de sopa"
                            },
                            {
                                "id": 2,
                                "name": "sal",
                                "unit": "colheres de café"
                            },
                            {
                                "id": 3,
                                "name": "farinha de trigo",
                                "unit": "gramas"
                            }
                        ]
                    }

        /get-ingredient - gets one ingredient's info by name
            # Request Method:
                POST

            # body:
                JSON
                {
                    "name": "azeite"
                }

            # response:
                JSON
                {
                    "id": 10,
                    "name": "azeite",
                    "unit": "colheres de sopa"
                }

        /add-ingredient - adds one new ingredient to the database
            # Request Method:
                POST

            # body:
                JSON
                Example:
                    {
                        "name": "morango",
                        "unit": "unidades"
                    }


            # response:
                JSON
                Example:
                    {
                        "id": 17,
                        "name": "morango",
                        "unit": "unidades"
                    }

        /show-recipes - shows all recipes in the database
            # Request Method:
                GET

            # response:
                JSON
                Example:
                    {
                        "recipes": [
                            {
                                "cost": 12,
                                "howto": "Molho:\n1- Descasque os tomates e as cebolas.\n2- Refogue os tomates a cebolas no óleo até dourar\n3- Adiciona o molho de tomate e sal ao molho\nMacarrão:\n1- Cozinhe o spaghetti por 20 minutos.\n2- Após cozido,  retire a água e adicione o molho",
                                "id": 1,
                                "ingredients": [
                                    {
                                        "id": 1,
                                        "ingredient": {
                                            "id": 2,
                                            "name": "sal",
                                            "unit": "colheres de café"
                                        },
                                        "quantity": 2
                                    },
                                    {
                                        "id": 2,
                                        "ingredient": {
                                            "id": 4,
                                            "name": "tomate",
                                            "unit": "unidades"
                                        },
                                        "quantity": 4
                                    },
                                    {
                                        "id": 3,
                                        "ingredient": {
                                            "id": 5,
                                            "name": "cebola",
                                            "unit": "unidades"
                                        },
                                        "quantity": 2
                                    },
                                    {
                                        "id": 4,
                                        "ingredient": {
                                            "id": 9,
                                            "name": "óleo de soja",
                                            "unit": "colheres de sopa"
                                        },
                                        "quantity": 1
                                    },
                                    {
                                        "id": 5,
                                        "ingredient": {
                                            "id": 12,
                                            "name": "spaghetti",
                                            "unit": "gramas"
                                        },
                                        "quantity": 100
                                    }
                                ],
                                "portions": 4,
                                "revenue": 20,
                                "title": "Macarronada Fácil"
                            },
                            {
                                "cost": 7,
                                "howto": "1- Lave o arroz\n2- Refogue o alho até dourar\n3- Acidione o arroz,  o sál e água até cobrir\n4- Cozinhe por 15 minutos - adiciona água se necessário",
                                "id": 2,
                                "ingredients": [
                                    {
                                        "id": 6,
                                        "ingredient": {
                                            "id": 2,
                                            "name": "sal",
                                            "unit": "colheres de café"
                                        },
                                        "quantity": 1
                                    },
                                    {
                                        "id": 7,
                                        "ingredient": {
                                            "id": 13,
                                            "name": "arroz",
                                            "unit": "xícaras de chá"
                                        },
                                        "quantity": 1
                                    },
                                    {
                                        "id": 8,
                                        "ingredient": {
                                            "id": 14,
                                            "name": "alho",
                                            "unit": "dentes"
                                        },
                                        "quantity": 1
                                    }
                                ],
                                "portions": 4,
                                "revenue": 10,
                                "title": "Arroz Rápido"
                            },
                            {
                                "cost": 2,
                                "howto": "1- Cozinhe o milho em águar fervendo por 10 minutos\n2- Adicione o sal",
                                "id": 3,
                                "ingredients": [
                                    {
                                        "id": 9,
                                        "ingredient": {
                                            "id": 2,
                                            "name": "sal",
                                            "unit": "colheres de café"
                                        },
                                        "quantity": 1
                                    },
                                    {
                                        "id": 10,
                                        "ingredient": {
                                            "id": 15,
                                            "name": "milho",
                                            "unit": "espigas"
                                        },
                                        "quantity": 1
                                    }
                                ],
                                "portions": 1,
                                "revenue": 5,
                                "title": "Milho Cozido"
                            }
                        ]
                    }


        /get-recipe - gets one recipe's info by id
            # Request Method:
                POST

            # body:
                JSON
                Example:
                    {
                        "id": 1
                    }

            # response:
                JSON
                Example:
                    {
                        "cost": 12,
                        "howto": "Molho:\n1- Descasque os tomates e as cebolas.\n2- Refogue os tomates a cebolas no óleo até dourar\n3- Adiciona o molho de tomate e sal ao molho\nMacarrão:\n1- Cozinhe o spaghetti por 20 minutos.\n2- Após cozido,  retire a água e adicione o molho",
                        "id": 1,
                        "ingredients": [
                            {
                                "id": 1,
                                "ingredient": {
                                    "id": 2,
                                    "name": "sal",
                                    "unit": "colheres de café"
                                },
                                "quantity": 2
                            },
                            {
                                "id": 2,
                                "ingredient": {
                                    "id": 4,
                                    "name": "tomate",
                                    "unit": "unidades"
                                },
                                "quantity": 4
                            },
                            {
                                "id": 3,
                                "ingredient": {
                                    "id": 5,
                                    "name": "cebola",
                                    "unit": "unidades"
                                },
                                "quantity": 2
                            },
                            {
                                "id": 4,
                                "ingredient": {
                                    "id": 9,
                                    "name": "óleo de soja",
                                    "unit": "colheres de sopa"
                                },
                                "quantity": 1
                            },
                            {
                                "id": 5,
                                "ingredient": {
                                    "id": 12,
                                    "name": "spaghetti",
                                    "unit": "gramas"
                                },
                                "quantity": 100
                            }
                        ],
                        "portions": 4,
                        "revenue": 20,
                        "title": "Macarronada Fácil"
                    }


        /add-recipe - adds one new recipe to the database
            # Request Method:
                POST

            # body:
                JSON
                Example:
                    {
                        "cost": 3,
                        "howto": "Descasque os tomates e refogue com o sal, azeite e alho.\nAdicione água até obter a textura desejada.",
                        "ingredients": [
                            {
                                "name": "sal",
                                "quantity": 2
                            },
                            {
                                "name": "tomate",
                                "quantity": 4
                            },
                            {
                                "name": "alho",
                                "quantity": 1

                            },
                            {
                                "name": "azeite",
                                "quantity": 1
                            }
                        ],
                        "portions": 4,
                        "revenue": 10,
                        "title": "Sopa de Tomate"
                    }

            # response:
                JSON
                Example:
                    {
                        "cost": 3,
                        "howto": "Descasque os tomates e refogue com o sal, azeite e alho.\nAdicione água até obter a textura desejada.",
                        "id": 4,
                        "ingredients": [
                            {
                                "id": 11,
                                "ingredient": {
                                    "id": 2,
                                    "name": "sal",
                                    "unit": "colheres de café"
                                },
                                "quantity": 2
                            },
                            {
                                "id": 12,
                                "ingredient": {
                                    "id": 4,
                                    "name": "tomate",
                                    "unit": "unidades"
                                },
                                "quantity": 4
                            },
                            {
                                "id": 13,
                                "ingredient": {
                                    "id": 14,
                                    "name": "alho",
                                    "unit": "dentes"
                                },
                                "quantity": 1
                            },
                            {
                                "id": 14,
                                "ingredient": {
                                    "id": 10,
                                    "name": "azeite",
                                    "unit": "colheres de sopa"
                                },
                                "quantity": 1
                            }
                        ],
                        "portions": 4,
                        "revenue": 10,
                        "title": "Sopa de Tomate"
                    }


        /optimize-production - Find the optimal production based on inventory ingredients
            # Request Method:
                POST

            # body:
                JSON
                Example:
                    {
                        "ingredients": [
                            {"name": "sal", "quantity": 4},
                            {"name": "milho", "quantity": 1},
                            {"name": "azeite", "quantity": 2},
                            {"name": "tomate", "quantity": 4},
                            {"name": "cebola", "quantity": 4},
                            {"name": "spaghetti", "quantity": 2},
                            {"name": "alho", "quantity": 4},
                            {"name": "batata", "quantity": 1},
                            {"name": "manteiga", "quantity": 2},
                            {"name": "açúcar", "quantity": 4},
                            {"name": "óleo de soja", "quantity": 4},
                            {"name": "arroz", "quantity": 2}
                        ]
                    }

            # response:
                JSON
                Example:
                    {
                        "Z": 9.0,
                        "recipes": [
                            {
                                "1": 0.0
                            },
                            {
                                "2": 2.0
                            },
                            {
                                "3": 1.0
                            }
                        ]
                    }

        /optimize-profif - Find the optimal profit based on inventory ingredients
            # Request Method:
                POST

            # body:
                JSON
                Example:
                    {
                        "ingredients": [
                            {"name": "sal", "quantity": 4},
                            {"name": "milho", "quantity": 1},
                            {"name": "azeite", "quantity": 2},
                            {"name": "tomate", "quantity": 4},
                            {"name": "cebola", "quantity": 4},
                            {"name": "spaghetti", "quantity": 2},
                            {"name": "alho", "quantity": 4},
                            {"name": "batata", "quantity": 1},
                            {"name": "manteiga", "quantity": 2},
                            {"name": "açúcar", "quantity": 4},
                            {"name": "óleo de soja", "quantity": 4},
                            {"name": "arroz", "quantity": 2}
                        ]
                    }

            # response:
                JSON
                Example:
                    {
                        "Z": 9.0,
                        "recipes": [
                            {
                                "1": 0.0
                            },
                            {
                                "2": 2.0
                            },
                            {
                                "3": 1.0
                            }
                        ]
                    }

### Frontend
