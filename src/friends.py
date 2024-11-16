from pathlib import Path
import os
from collect import collect_participants

def friends(a,b):
    if b.id in a.friends:
        return True
    return False

def bidirectional_friends(a,b)->bool:
    if friends(a,b) and friends(b,a):
        return True
    return False

DATA_FILE = Path(os.path.dirname(__file__)).resolve().parent / "data" / "participants-prova.json"

participants = collect_participants(DATA_FILE)
for participant in participants:
    participant.friend_registration