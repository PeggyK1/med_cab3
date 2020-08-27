from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, data, effects, ailments, flavors

app = FastAPI(
    title='Med Cabinet 3 DS API',
    description="""Recommend  cannabis strain based on User input of
     ailment, desired effect, desired flavor, and location.""",
    version='0.1',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(data.router)
app.include_router(effects.router)
app.include_router(ailments.router)
app.include_router(flavors.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
