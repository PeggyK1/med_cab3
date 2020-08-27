import logging
import random
import pandas as pd

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

strain = pd.read_csv('data/strains.csv')
strain_list = strain['name']

class Strain(BaseModel):
    """Use this data model to parse the request body JSON."""

    ailment: str = Field(..., example='Depression')
    effect: str = Field(..., example='Happy')
    flavor: str = Field(..., example='Citrus')
    location: str = Field(..., example='Los Angeles, CA')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])



@router.post('/predict')
async def predict(strain: Strain):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `ailment`: string
    - `effect`: string
    - `flavor`: string
    - `location`: string

    ### Response
    - `prediction`: string
    """

    X_new = strain.to_df()
    log.info(X_new)
    y_pred = random.choice(strain_list)
    return {
        'prediction': y_pred
    }
