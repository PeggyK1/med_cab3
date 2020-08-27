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

@router.get('/effects')
async def effects():
    """
    Return effects data as json
    """
    anxious = []
    tingly = []
    paranoid = []
    horny = []
    happy = []
    energetic = []
    talkative = []
    relaxed = []
    dry_mouth = []
    hungry = []
    euphoric = []
    sleepy = []
    uplifted = []
    creative = []
    focused = []

    for i in list(range(len(strain))):
        if 'Anxious' in strain['effects'][i]:
            anxious.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Tingly' in strain['effects'][i]:
            tingly.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Paranoid' in strain['effects'][i]:
            paranoid.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Horny' in strain['effects'][i]:
            horny.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Happy' in strain['effects'][i]:
            happy.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Energetic' in strain['effects'][i]:
            energetic.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Talkative' in strain['effects'][i]:
            talkative.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Relaxed' in strain['effects'][i]:
            relaxed.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Dry Mouth' in strain['effects'][i]:
            dry_mouth.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Hungry' in strain['effects'][i]:
            hungry.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Euphoric' in strain['effects'][i]:
            euphoric.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Sleepy' in strain['effects'][i]:
            sleepy.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Uplifted' in strain['effects'][i]:
            uplifted.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Creative' in strain['effects'][i]:
            creative.append(strain['name'][i])
    for i in list(range(len(strain))):
        if 'Focused' in strain['effects'][i]:
            focused.append(strain['name'][i])
    
    json_anxious = json.dumps(anxious)
    json_tingly = json.dumps(tingly)
    json_paranoid = json.dumps(paranoid)
    json_horny = json.dumps(horny)
    json_happy = json.dumps(happy)
    json_energetic = json.dumps(energetic)
    json_talkative = json.dumps(talkative)
    json_relaxed = json.dumps(relaxed)
    json_dry_mouth = json.dumps(dry_mouth)
    json_hungry = json.dumps(hungry)
    json_euphoric = json.dumps(euphoric)
    json_sleepy = json.dumps(sleepy)
    json_uplifted = json.dumps(uplifted)
    json_creative = json.dumps(creative)
    json_focused = json.dumps(focused)

    return json_anxious, json_tingly, json_paranoid, json_horny, json_happy, json_energetic, json_talkative, json_relaxed, json_dry_mouth, json_hungry, json_euphoric, json_sleepy, json_uplifted, json_creative, json_focused