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


@router.get('/ailments')
async def ailments():
    """
    Return ailments data as json
    """
    nausea = []
    depression = []
    lack_of_appetite = []
    inflammation = []
    stress = []
    insomnia = []
    seizures = []
    muscle_spasms = []
    pain = []

    for i in list(range(len(strain))):
        if 'Nausea' in strain['ailment'][i]:
            nausea.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Depression' in strain['ailment'][i]:
            depression.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Lack of Appetite' in strain['ailment'][i]:
            lack_of_appetite.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Inflammation' in strain['ailment'][i]:
            inflammation.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Stress' in strain['ailment'][i]:
            stress.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Insomnia' in strain['ailment'][i]:
            insomnia.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Seizures' in strain['ailment'][i]:
            seizures.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Muscle Spasms' in strain['ailment'][i]:
            muscle_spasms.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Pain' in strain['ailment'][i]:
            pain.append(strain['name'][i])

    json_nausea = json.dumps(nausea)
    json_depression = json.dumps(depression)
    json_lack_of_appetitie = json.dumps(lack_of_appetite)
    json_inflammation = json.dumps(inflammation)
    json_stress = json.dumps(stress)
    json_insomnia = json.dumps(insomnia)
    json_seizures = json.dumps(seizures)
    json_muscle_spasms = json.dumps(muscle_spasms)
    json_pain = json.dumps(pain)

    return 'nausea', json_nausea, 'depression', json_depression,\
      'loa', json_lack_of_appetitie, 'inflammation', json_inflammation,\
      'stress', json_stress, 'insomnia', json_insomnia,'seizures', json_seizures,\
      'muscle_spasm', json_muscle_spasms, 'pain', json_pain
