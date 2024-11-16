
import yogi
from collect import collect_participants
from group import Group


def main() -> None:
    participants = collect_participants(yogi.read(str))

    a = (Group(participants[0]))

    print(a)

    # PRIMER MIREM ELS CASOS QUE S'HAN DE COMPLIR SÍ O SÍ

    # DESPRÉS ELS QUE SÓN MOLT IMPORTANT

    # FINALMENT ÚLTIMES COSETES QUE SUMEN PUNTS

if __name__ == "__main__":
    main()