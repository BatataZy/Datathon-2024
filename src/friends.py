from pathlib import Path
import os
from collect import collect_participants
from yogi import read

def friends(a,b):
    if b.id in a.friends:
        return True
    return False
 
def bidirectional_friends(a,b)->bool:
    if friends(a,b) and friends(b,a):
        return True
    return False

DATA_FILE = Path(os.path.dirname(__file__)).resolve().parent / "data" / "participants-prova.json"

participants = collect_participants(read(str)) # C:/Users/GABO.LOPEZ/Documents/GitHub/AEDChallenge/data/datathon_participants.json
for participant in participants:
    print(participant.friend_registration)