<<<<<<< HEAD
from friends import 
def main() -> None:
    ...
=======

import yogi
from collect import collect_participants
from group import Group, participant_to_group


def main() -> None:
    participants = collect_participants(yogi.read(str)) #/home/max/Datathon/Datathon-2024/data/datathon_participants.json

    print([participants[0].id, participants[1].id])

    print(participant_to_group(participants[3]).friend_registration + participant_to_group(participants[3]).friend_registration)

>>>>>>> 869d93b8fe628a788ec95616ad223076e61e1d43
    # PRIMER MIREM ELS CASOS QUE S'HAN DE COMPLIR SÍ O SÍ

    # DESPRÉS ELS QUE SÓN MOLT IMPORTANT

    # FINALMENT ÚLTIMES COSETES QUE SUMEN PUNTS

if __name__ == "__main__":
    main()