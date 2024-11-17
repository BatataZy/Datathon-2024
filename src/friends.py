from pathlib import Path
import os
from collect import collect_participants

def friends(a,b) -> bool:
    if b.ids in a.friend_registration:
        return True
    return False
 
def bidirectional_friends(a,b)->bool:
    if friends(a,b) and friends(b,a):
        return True
    return False

