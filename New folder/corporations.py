import io
import random

GroupNames = open("group_names.txt", "a")
CorpNamesFirstPart = ["Andromeda", "Secundus", "Pythagoras", "Gemini", "Juggernaut", "Prometheus", "Sephirah", "Qlipoth", "Orlumbus", "Melody", "Limbus"]
CorpNamesSecondPart = ["Collective", "Foundation", "Company", "Corporation", "Section", "Domain", "Dominion"]

def Choose(array):
    maxSize = len(array) - 1
    choice = random.randint(0,maxSize)

    return array[choice]



i = 0
#while i != 100:
#    CorpName = "The " + Choose(CorpNamesFirstPart) + " " + Choose(CorpNamesSecondPart)
#    print(CorpName)
#    GroupNames.write(CorpName + "\n")
#    i += 1

#GroupNames.close()