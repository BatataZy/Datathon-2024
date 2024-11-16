from typing import Dict

from collect import RawParticipant
from objectiu import objective_level
from dataclasses import dataclass

@dataclass
class Group:

    def __init__(self, participant:RawParticipant):
        self.participants = participant.id
        self.friend_registration = participant.friend_registration
        self.preferred_languages = participant.preferred_languages
        self.availability = participant.availability
        self.objective = objective_level(participant.objective)
        self.remaining_team_size = participant.preferred_team_size - 1
        self.interest_in_challenges = dict()#(i for i in participant.interest_in_challenges), 1)
        self.roles = [participant.preferred_role]
        
        match participant.experience_level:
            case "Beginner": self.experience_level = 1.
            case "Intermediate": self.experience_level = 2.
            case "Advanced":  self.experience_level = 3.
        
        match participant.year_of_study:
            case "1st year": self.year_of_study = 1.
            case "2nd year": self.year_of_study = 2.
            case "3rd year": self.year_of_study = 3.
            case "4th year": self.year_of_study = 4.
            case "Masters": self.year_of_study = 5.
            case "PhD": self.year_of_study = 6.
        
        self.programming_skills = participant.programming_skills
        self.hackathons_done = float(participant.hackathons_done)
        self.interests = participant.interests
        self.university = dict()#participant.university, 1)


    participants: list[str]

    #Ordered list of main points
    friend_registration: list[str]
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

def grouping(first: Group, second: Group) -> Group:
    new:Group = []
