def friends(a,b):
    """
    if a.friends == b.id:
        return True
    return False
    """

def bidirectional_friends(a,b)->bool:
    if friends(a,b) and friends(b,a):
        return True
    return False