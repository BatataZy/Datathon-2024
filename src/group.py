from typing import Dict, Set

from collect import RawParticipant
from objectiu import objective_level
from dataclasses import dataclass

@dataclass
class Group:

    ids: Set[str]

    #Ordered list of main points
    friend_registration: Set[str]
    preferred_languages: Set[str]
    availability: Set[str]
    objective: int
    preferred_team_size: int
    interest_in_challenges: Dict[str, int]
    roles: Set[str]
    experience_level: float
    year_of_study: float
    programming_skills: Dict[str, int]
    hackathons_done: float
    interests: Set[str]

    #Group generator function from participant data
    def __init__(self, ids, friend_registration, preferred_languages, availability, objective, preferred_team_size, interest_in_challenges, roles, experience_level, year_of_study, programming_skills, hackathons_done, interests):
        self.ids = ids
        self.friend_registration = friend_registration
        self.preferred_languages = preferred_languages
        self.availability = availability
        self.objective = objective
        self.preferred_team_size = preferred_team_size
        self.interest_in_challenges = interest_in_challenges
        self.roles = roles
        self.experience_level = experience_level
        self.year_of_study = year_of_study
        self.programming_skills = programming_skills
        self.hackathons_done = hackathons_done
        self.interests = interests

    def __add__(self, other):

        interest_in_challenges = dict([])
        for i in (set(list(self.interest_in_challenges)) | set(list(other.interest_in_challenges))):
            interest_in_challenges.setdefault(i, self.interest_in_challenges.get(i, 0) + other.interest_in_challenges.get(i, 0))

        programming_skills = dict([])
        for i in (set(list(self.programming_skills)) | set(list(self.programming_skills))):
            programming_skills.setdefault(i, max(self.programming_skills.get(i, 0), other.programming_skills.get(i, 0)))
                
        return Group(
            self.ids | other.ids,
            self.friend_registration & other.friend_registration,
            self.preferred_languages & other.preferred_languages,
            self.availability | other.availability,
            (self.objective*len(self.ids) + other.objective*len(other.ids))/(len(self.ids) + len(other.ids)),
            (self.preferred_team_size*len(self.ids) + other.preferred_team_size*len(other.ids))/(len(self.ids) + len(other.ids)),
            interest_in_challenges,
            self.roles | other.roles,
            (self.experience_level*len(self.ids) + other.experience_level*len(other.ids))/(len(self.ids) + len(other.ids)),
            (self.year_of_study*len(self.ids) + other.year_of_study*len(other.ids))/(len(self.ids) + len(other.ids)),
            programming_skills,
            (self.hackathons_done*len(self.ids) + other.hackathons_done*len(other.ids))/(len(self.ids) + len(other.ids)),
            self.interests | other.interests,
        )

def participant_to_group(participant:RawParticipant) -> Group:

    ids = set([participant.id])
    friend_registration = set(participant.friend_registration)
    preferred_languages = set(participant.preferred_languages)
    availability = set(i for i in list(participant.availability) if participant.availability.get(i) == True)
    objective = objective_level(participant.objective)
    preferred_team_size = participant.preferred_team_size
    interest_in_challenges = dict((i, 1) for i in participant.interest_in_challenges)
    roles = set([participant.preferred_role])
    
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
    interests = set(participant.interests)

    return Group(ids, friend_registration, preferred_languages, availability, objective, preferred_team_size, interest_in_challenges, roles, experience_level, year_of_study, programming_skills, hackathons_done, interests)