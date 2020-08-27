import logging
from os import getenv, listdir
import pandas as pd
from fastapi import APIRouter
import json


log = logging.getLogger(__name__)
router = APIRouter()

print(listdir())
REPO_FILEPATH = getenv('REPO_FILEPATH')
strain = pd.read_csv('data/strains.csv')

@router.get('/flavors')
async def flavors():
    """
    Return flavors data as json
    """
    berry = []
    apple = []
    honey = []
    mango = []
    earthy = []
    mint = []
    blueberry = []
    ammonia = []
    coffee = []
    vanilla = []
    rose = []
    pine = []
    citrus = []
    sweet = []
    pineapple = []
    skunk = []
    orange = []
    strawberry = []
    lemon = []
    grape = []
    lime = []
    pepper = []
    lavender = []

    for i in list(range(len(strain))):
        if 'Coffee' in strain['flavor'][i]:
            coffee.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Pepper' in strain['flavor'][i]:
            pepper.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Lavender' in strain['flavor'][i]:
            lavender.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Mango' in strain['flavor'][i]:
            mango.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Earthy' in strain['flavor'][i]:
            earthy.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Citrus' in strain['flavor'][i]:
            citrus.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Lemon' in strain['flavor'][i]:
            lemon.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Strawberry' in strain['flavor'][i]:
            strawberry.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Pine' in strain['flavor'][i]:
            pine.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Vanilla' in strain['flavor'][i]:
            vanilla.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Honey' in strain['flavor'][i]:
            honey.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Pineapple' in strain['flavor'][i]:
            pineapple.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Blueberry' in strain['flavor'][i]:
            blueberry.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Orange' in strain['flavor'][i]:
            orange.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Skunk' in strain['flavor'][i]:
            skunk.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Grape' in strain['flavor'][i]:
            grape.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Berry' in strain['flavor'][i]:
            berry.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Lime' in strain['flavor'][i]:
            lime.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Rose' in strain['flavor'][i]:
            rose.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Sweet' in strain['flavor'][i]:
            sweet.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Apple' in strain['flavor'][i]:
            apple.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Mint' in strain['flavor'][i]:
            mint.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Ammonia' in strain['flavor'][i]:
            ammonia.append(strain['name'][i])

    json_berry = json.dumps(berry)
    json_apple = json.dumps(apple)
    json_honey = json.dumps(honey)
    json_mango = json.dumps(mango)
    json_earthy = json.dumps(earthy)
    json_mint = json.dumps(mint)
    json_bluberry = json.dumps(blueberry)
    json_ammonia = json.dumps(ammonia)
    json_coffee = json.dumps(coffee)
    json_vanilla = json.dumps(vanilla)
    json_rose = json.dumps(rose)
    json_pine = json.dumps(pine)
    json_citrus = json.dumps(citrus)
    json_sweet = json.dumps(sweet)
    json_pineapple = json.dumps(pineapple)
    json_skunk = json.dumps(skunk)
    json_orange = json.dumps(orange)
    json_strawberry = json.dumps(strawberry)
    json_lemon = json.dumps(lemon)
    json_grape = json.dumps(grape)
    json_lime = json.dumps(lime)
    json_pepper = json.dumps(pepper)
    json_lavender = json.dumps(lavender)

    return json_berry, json_apple, json_honey, json_mango, json_earthy, json_mint, json_bluberry, json_ammonia, json_coffee, json_vanilla, json_rose, json_pine, json_citrus, json_sweet, json_pineapple, json_skunk, json_orange, json_strawberry, json_lemon, json_grape, json_lime, json_pepper, json_lavender

