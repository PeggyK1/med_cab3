from os import getenv
import pandas as pd


REPO_FILEPATH = getenv('REPO_FILEPATH')
strain = pd.read_csv(REPO_FILEPATH + '\data\final_strains.csv')


results = strain.to_json(orient="index")
parsed = json.loads(results)
json.dumps(parsed, indent=4)
