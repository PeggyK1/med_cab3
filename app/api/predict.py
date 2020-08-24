import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Strain(BaseModel):
    """Use this data model to parse the request body JSON."""

    ailment: str = Field(..., example='Depression')
    effect: str = Field(..., example='Happy')
    flavor: str = Field(..., example='Citrus')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value


@router.post('/predict')
async def predict(item: Strain):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `ailment`: string
    - `effect`: string
    - `flavor`: string

    ### Response
    - `prediction`: string
    """

    X_new = item.to_df()
    log.info(X_new)
    y_pred = 'Indica'
    return {
        'prediction': y_pred,
    }
