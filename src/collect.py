from typing import Dict
import json
from dataclasses import dataclass

@dataclass
class RawParticipant:
    
    id: str

    #User presentation
    introduction: str
    name: str
    age: int
    email: str

    #Don't know what to do yet
    fun_fact: str
    future_excitement: str
    technical_project: str

    #Ordered list of main points
    friend_registration: set[str]
    preferred_languages: list[str]
    availability: Dict[str, bool]
    objective: str
    preferred_team_size: int
    interest_in_challenges: list[str]
    preferred_role: str
    experience_level: str
    year_of_study: str
    programming_skills: Dict[str, int]
    hackathons_done: int
    interests: list[str]
    university: str

    #Useless
    shirt_size: str
    dietary_restrictions: str

def collect_participants(path: str) -> list[RawParticipant]:

    participants = []

    try: 
        for x in json.load(open(path)):
            participants.append(RawParticipant(**x))

    except: 
        raise Exception(f"There was an error loading the participants. Are you using the correct path and file?")

    return participants
