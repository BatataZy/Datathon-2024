import re
from collect import collect_participants
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
    def is_negated(text, keyword):
        negative_patterns = [rf"{neg}.*\b{keyword}\b" for neg in negations]
        for pattern in negative_patterns:
            if re.search(pattern, text):
                return True
        return False

    # Count matches for each category
    score_1 = sum(not is_negated(text, word) and word in text for word in option_1_keywords)
    score_2 = sum(not is_negated(text, word) and word in text for word in option_2_keywords)
    score_3 = sum(not is_negated(text, word) and word in text for word in option_3_keywords)

    # Determine the option with the highest score
    scores = [score_1, score_2, score_3]
    option = scores.index(max(scores)) + 1

    return option



participants = collect_participants(yogi.read(int)) # "/home/max/Datathon/AEDChallenge/data/datathon_participants.json"
print(participants)

