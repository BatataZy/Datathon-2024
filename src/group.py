from typing import Dict

from collect import RawParticipant
from objectiu import objective_level
from dataclasses import dataclass

@dataclass
class Group:

    participants: list[str]

    #Ordered list of main points
    friend_registration: set[str]
    preferred_languages: list[str]
    availability: Dict[str, bool]
    objective: int
    remaining_team_size: int
    interest_in_challenges: Dict[str, int]
    roles: list[str]
    experience_level: float
    year_of_study: float
    programming_skills: Dict[str, int]
    hackathons_done: float
    interests: list[str]
    university: Dict[str, int]

    #Group generator function from participant data
    def __init__(self, participants, friend_registration, preferred_languages, availability, objective, remaining_team_size, interest_in_challenges, roles, experience_level, year_of_study, programming_skills, hackathons_done, interests, university):
        self.participants = participants
        self.friend_registration = friend_registration
        self.preferred_languages = preferred_languages
        self.availability = availability
        self.objective = objective
        self.remaining_team_size = remaining_team_size
        self.interest_in_challenges = interest_in_challenges
        self.roles = roles
        self.experience_level = experience_level
        self.year_of_study = year_of_study
        self.programming_skills = programming_skills
        self.hackathons_done = hackathons_done
        self.interests = interests
        self.university = university

    def __add__(self, other):
        return Group(
            self.participants + other.participans,
            self.friend_registration - self.friend_registration
        )

def participant_to_group(participant:RawParticipant) -> Group:

    participants = [participant.id]
    friend_registration = participant.friend_registration
    preferred_languages = participant.preferred_languages
    availability = participant.availability
    objective = objective_level(participant.objective)
    remaining_team_size = participant.preferred_team_size - 1
    interest_in_challenges = dict((i, 1) for i in participant.interest_in_challenges)
    roles = [participant.preferred_role]
    
    match participant.experience_level:
        case "Beginner": experience_level = 1.
        case "Intermediate": experience_level = 2.
        case "Advanced":  experience_level = 3.
    
    match participant.year_of_study:
        case "1st year": year_of_study = 1.
        case "2nd year": year_of_study = 2.
        case "3rd year": year_of_study = 3.
        case "4th year": year_of_study = 4.
        case "Masters": year_of_study = 5.
        case "PhD": year_of_study = 6.
    
    programming_skills = participant.programming_skills
    hackathons_done = float(participant.hackathons_done)
    interests = participant.interests
    university = dict([(participant.university, 1)])

    return Group(participants, friend_registration, preferred_languages, availability, objective, remaining_team_size, interest_in_challenges, roles, experience_level, year_of_study, programming_skills, hackathons_done, interests, university)
