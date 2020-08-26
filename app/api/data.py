from os import getenv
import pandas as pd
from fastapi import APIRouter



@router.post('/data')
async def data():
    """
    Return cannabis data as json
    """

    REPO_FILEPATH = getenv('REPO_FILEPATH')
    strain = pd.read_csv(REPO_FILEPATH + '\data\final_strains.csv')


    results = strain.to_json(orient="index")

    return results
