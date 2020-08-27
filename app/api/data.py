import logging
from os import getenv
import pandas as pd
from fastapi import APIRouter


log = logging.getLogger(__name__)
router = APIRouter()


REPO_FILEPATH = getenv('REPO_FILEPATH')
strain = pd.read_csv('\data\strains.csv')
results = strain.to_json(orient="index")

@router.get('/data')
async def data():
    """
    Return cannabis data as json
    """
    return results
