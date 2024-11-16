import re
import yogi
from collect import RawParticipant, collect_participants
def objective_level(text:str):
    # Paraules clau per a cada opció
    option_1_keywords = [
        "win", "compete", "challenge", "top", "victory", "success", 
        "competitive", "push myself", "outdo", "glory", "focus", "intensely", 
        "achievement", "first place", "long hours", "perfect my project"
    ]
    option_2_keywords = [
        "learn", "grow", "improve", "skills", "level up", "new technologies",
        "techniques", "ideas", "challenge myself", "collaborate", 
        "support", "exposure", "develop", "better", "next level"
    ]
    option_3_keywords = [
        "fun", "friends", "connections", "enjoy", "stress-free", "atmosphere", 
        "experience", "blast", "soak up", "community", "relax", "networking", 
        "new people", "workshop", "meetup", "food", "participate in activities"
    ]
    # Paraules de negació
    negations = ["not", "never", "no", "none", "without", "don't"]

    # Funció auxiliar per detectar si hi ha negació abans d'una paraula clau
    def has_negation(text: str, keyword: str) -> bool:
        pattern = r"(\b(?:{})\b)\s+\b{}\b".format("|".join(negations), re.escape(keyword))
        return bool(re.search(pattern, text, re.IGNORECASE))

    # Inicialitzar comptadors
    score_1, score_2, score_3 = 0, 0, 0

    # Convertir el text a minúscules per a facilitar la comparació
    text = text.lower()

    # Comprovar paraules clau i comptar puntuacions
    for word in option_1_keywords:
        if word in text and not has_negation(text, word):
            score_1 += 1
    for word in option_2_keywords:
        if word in text and not has_negation(text, word):
            score_2 += 1
    for word in option_3_keywords:
        if word in text and not has_negation(text, word):
            score_3 += 1

    # Determinar el cas segons el màxim score
    if score_1 > score_2 and score_1 > score_3:
        return 3
    elif score_2 > score_1 and score_2 > score_3:
        return 2
    else:
        return 1

#participants: list[RawParticipant] = collect_participants(yogi.read(str)) # "C:/Users/GABO.LOPEZ/Documents/GitHub/AEDChallenge/data/datathon_participants.json"

#for participant in participants:
#    print(participant.objective)
#    print(determine_objective_level(participant.objective))
#print(determine_objective_level("Hey, I'm Rosa! For this datathon, my objective is to come out with a learning mentality. I want to dive deeper into data analysis and try new tools to enhance my skills. I'd love to challenge myself to build complex projects and troubleshoot problems. I'm not particularly worried about winning or taking the top spot, but I do hope to get exposure to new data manipulation techniques and frameworks. By the end of this datathon, I'd like to feel confident in taking on more ambitious projects and having a fresh perspective to approach data science problems."))
