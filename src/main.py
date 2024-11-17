from linecache import updatecache
from typing import Dict
import yogi
from collect import RawParticipant, collect_participants
from group import Group, participant_to_group
from friends import bidirectional_friends
import group
from objectiu import objective_level

def algorithm(grups: list[Group]) -> list[Group]:

    output = []
    ranking = dict()
    popularity = [0] * len(grups)

    for i in range(len(grups)): # Anem afegint persona a persona
        it = 0

        popu_max = (0, 0)

        if grups[i].preferred_team_size <= len(grups[i].ids): pass

        for j in range(len(grups)):

            popu = 0

            it += 1
            if i != j and grups[j].preferred_team_size > len(grups[j].ids) and 4 >= (grups[i].preferred_team_size*len(grups[i].ids) + grups[j].preferred_team_size*len(grups[j].ids))/(len(grups[i].ids) + len(grups[j].ids)) >= (len(grups[i].ids | grups[j].ids)):

                seriousness = (grups[i].objective*len(grups[i].ids) + grups[j].objective*len(grups[j].ids))/(len(grups[i].ids)+len(grups[j].ids))

                if bidirectional_friends(grups[i], grups[j]): popu += 1009
                if grups[i].preferred_languages & grups[j].preferred_languages != set([]): popu += 499
                popu += 17 * len(grups[i].availability & grups[j].availability)**2
                popu += 127 * (-(abs( grups[i].objective - grups[j].objective ))**2 + 4)
                popu += 19 * (-( grups[i].preferred_team_size - grups[j].preferred_team_size )**3 + 8)

                popu += seriousness**2 * ( -( (grups[i].experience_level + grups[i].year_of_study) - (grups[j].experience_level + grups[j].year_of_study) )**2 + 49)
                popu += 0.5 * seriousness**2 * ( -abs(grups[i].programming_skills - grups[j].programming_skills)**2 + 100 )
                popu += 13 * seriousness**2 * len(grups[i].roles - grups[j].roles)
                popu += 3 * seriousness**2 * len(set(list(grups[i].interest_in_challenges)) & set(list(grups[j].interest_in_challenges)))

                popu += 2.5/(seriousness**2) * (-(grups[i].age - grups[j].age)**2 + 100)
                popu += 200/(seriousness**3) * len(grups[i].interests & grups[j].interests)

                if popu > popu_max[1]: popu_max = (j, popu)

            else: pass

        popularity[i] = popu_max[0]
        ranking.setdefault(popu_max[0], 0)
        ranking.update([(popu_max[0], 1 + ranking.get(popu_max[0]))])

    ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    garbell = [False] * len(grups)

    for i in ranking:
        if garbell[i[0]] == False and garbell[popularity[i[0]]] == False:
            output.append(grups[i[0]] + grups[popularity[i[0]]])
            garbell[i[0]] = True
            garbell[popularity[i[0]]] = True

    for i in range(len(garbell)):
        if garbell[i] == False:
            output.append(grups[i])

    return(output)

def compatibility(group: Group, participants: list[RawParticipant]) -> Dict[str, int]:
    compatibility = dict([(i, 0) for i in ("total", "language", "availability", "objective", "team_size", "challenge", "role", "experience", "skills", "age")])

    g_participants: list[Group] = []

    for i in group.ids:
        for j in participants:
                if j.id == i: g_participants.append(participant_to_group(j))

    compatibility.update([("language", min(len(group.preferred_languages), 1))])
    compatibility.update([("availability", sum([(len(i.availability & group.availability)/5) for i in g_participants]) / len(group.ids))])
    compatibility.update([("objective", sum([((3-abs(i.objective - group.objective))/3) for i in g_participants]) / len(group.ids))])
    compatibility.update([("team_size", sum([((2-abs(i.preferred_team_size - len(group.ids)))/2) for i in g_participants]) / len(group.ids))])
    compatibility.update([("challenge", sum([(min(len(set(list(i.interest_in_challenges)) & set(list(group.interest_in_challenges))), 1)) for i in g_participants]) / len(group.ids))])
    compatibility.update([("role", len(group.roles) / len(group.ids))])
    compatibility.update([("experience", sum([((7-abs((i.experience_level+i.year_of_study) - (group.experience_level+group.year_of_study)))/7) for i in g_participants]) / len(group.ids))])
    compatibility.update([("skills", sum([((9-abs(i.programming_skills - group.programming_skills))/9) for i in g_participants]) / len(group.ids))])
    compatibility.update([("age", sum([((10-abs(i.age - group.age))/10) for i in g_participants]) / len(group.ids))])

    compatibility.update([("total", (499*compatibility.get("language") + 425*compatibility.get("availability") + 508*compatibility.get("objective") + 152*compatibility.get("team_size") + 49*(compatibility.get("objective")**2)*compatibility.get("experience") + 9*(compatibility.get("objective")**2)*compatibility.get("challenge") + 13*(compatibility.get("objective")**2)*compatibility.get("role") + 50*(compatibility.get("objective")**2)*compatibility.get("skills") + 13/(compatibility.get("objective")**2)*compatibility.get("age"))/(499 + 425 + 508 + 152 + 49*(group.objective**2) + 9*(group.objective**2) + 50*(group.objective**2) + 13*(group.objective**2) + 250/(group.objective**2)))])

    return compatibility

def main() -> None: # C:/Users/GABO.LOPEZ/Documents/GitHub/Datathon-2024/data/datathon_participants.json

    print("Please type the path of the participants json file:")

    participants = collect_participants(yogi.read(str)) #/home/max/Datathon/Datathon-2024/data/datathon_participants.json
    grups: list[Group] = [participant_to_group(participant) for participant in participants]

    print("\nCalculating groups... (this may take a while)")

    it = 0
    old_length = 0
    length = len(grups)
    while old_length != length:

        it+=1

        grups = algorithm(grups)
        old_length, length = length, len(grups)

    print(f"\nDone! (in {it} iterations)")

    compatibilities = [(compatibility(i, participants).get("total", 0)) for i in grups]

    comp_copy = compatibilities[::]
    comp_copy.sort()

    mediana = (comp_copy[int(len(comp_copy)/2)])
    mitjana = (sum(comp_copy)/len(comp_copy))

if __name__ == "__main__":
    main()