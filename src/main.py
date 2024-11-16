import yogi
from collect import collect_participants
from group import Group, participant_to_group
from friends import bidirectional_friends

def main() -> None: # C:/Users/GABO.LOPEZ/Documents/GitHub/Datathon-2024/data/datathon_participants.json
    participants = collect_participants(yogi.read(str)) #/home/max/Datathon/Datathon-2024/data/datathon_participants.json

    grups: list[Group] = [participant_to_group(participant) for participant in participants]

    for equip in grups: # Anem afegint persona a persona
        compatibilitat: list[float] = [0] * len(participants) # Farem puntuació per cada persona per veure la compatibilitat
        # Primer mirem si té amics en comú per poder-los combinar directament
        if equip.friend_registration != set([]): # Si no està buit, fem els participants.
            for amic in equip.friend_registration:
                posicio = 0 # A revisar si podem utilitzar més cops.
                for x in grups: # Recorres TOTS ELS PARTICIPANTS
                    if amic in x.ids:
                        # AFEGIM FENT "ADD" EL equip A LA LLISTA TOTS ELS AMICS AL equip
                        for i in x.ids:
                            if bidirectional_friends(amic, i):
                                # AFEGIM FENT "ADD" EL equip A LA LLISTA TOTS ELS AMICS AL equip
                                equip = equip + x 
                                compatibilitat[posicio] = 0



                    posicio += 1
      # Fem el dels amics i l'afegim si encara no està

        # Mirem que tinguin el mateix llenguatge
        

        
    # PRIMER MIREM ELS CASOS QUE S'HAN DE COMPLIR SÍ O SÍ

    # DESPRÉS ELS QUE SÓN MOLT IMPORTANT
    

    # FINALMENT ÚLTIMES COSETES QUE SUMEN PUNTS


if __name__ == "__main__":
    main()