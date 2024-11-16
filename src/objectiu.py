import re
from collect import Participant, RawParticipant, collect_participants
import yogi

def classify_goal(text: str) -> int:
    """
    Classifies the text based on the participant's goal in the competition,
    taking negations into account and using an expanded keyword set.

    Args:
        text (str): The participant's response text.

    Returns:
        int: A number between 1 and 3 indicating seriousness about winning 
             (1 = very serious, 2 = mixed goals, 3 = focus on fun and experience).
    """
    text = text.lower()  # Normalize the text to lowercase

    # Expanded keywords for each classification
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

    # Negation words
    negations = ["not", "never", "no", "none", "without", "don't", ]

    # Helper function to check if a keyword is negated
    def is_negated(text: str, keyword: str) -> bool:
        negative_patterns = [rf"{neg}.*\b{keyword}\b" for neg in negations]
        for pattern in negative_patterns:
            if re.search(pattern, text):
                return True
        return False
    
    
    # Count matches for each category
    score_1 = 0
    for word in text:
        print(word)
    score_1 = sum(not is_negated(text, word) and word in text for word in option_1_keywords)

    score_2 = sum(not is_negated(text, word) and word in text for word in option_2_keywords)
    score_3 = sum(not is_negated(text, word) and word in text for word in option_3_keywords)

    # Determine the option with the highest score
    scores = [score_1, score_2, score_3]
    print(scores)
    option = scores.index(max(scores)) + 1 # Si hi ha dubte fiquem la menys comptetitiva

    return option


# participants: list[Participant] = collect_participants(yogi.read(str)) 
participants: list[RawParticipant] = collect_participants(yogi.read(str)) # "C:/Users/GABO.LOPEZ/Documents/GitHub/AEDChallenge/data/datathon_participants.json"

for participant in participants:
    print(participant.objective)
    print(classify_goal(participant.objective))

# Hey, I'm Rosa! For this datathon, my objective is to come out with a learning mentality. 
# I want to dive deeper into data analysis and try new tools to enhance my skills. 
# I'd love to challenge myself to build complex projects and troubleshoot problems.
#  I'm not particularly worried about winning or taking the top spot, but I do hope to get exposure to new data manipulation 
# techniques and frameworks. By the end of this datathon, I'd like to feel confident in taking on more ambitious projects and 
# having a fresh perspective to approach data science problems.
[2, 3, 0] # What happens in the "not particularly worried about winning?""