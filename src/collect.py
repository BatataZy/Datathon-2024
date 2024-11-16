from typing import Dict
import json

class Participant:
    
    id: str

    name: str
    email: str
    shirt_size: str
    age: int
    year_of_study: str
    university: str
    dietary_restrictions: str
    interests: list[str]
    preferred_role: str
    experience_level: str
    hackathons_done: str
    objective: str
    introduction: str
    technical_project: str
    future_excitement: str
    fun_fact: str
    preferred_languages: list[str]
    friend_registration: list[str]
    preferred_team_size: str
    availability: Dict[str, bool]
    programming_skills: Dict[str, int]
    interest_in_challenges: list[str]

def collect_participants(path: str) -> list[Participant]:

    participants = []

    try: 
        for x in json.load(open(path)):
            participants.append(Participant(**x))

    except: 
        raise Exception(f"There was an error loading the participants. Are you using the correct path and file?")

    return participants


