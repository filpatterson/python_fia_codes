from PersonConstruct import Person
from TouristTypeDB import PersonalitiesDB

#   initialize a database of all possible personalities
personsDB = PersonalitiesDB()

#   input all characteristics of person (small letters)
print("Input characteristics of the person using words with small letters (if there is no concrete characteristic print 'unknown' or 'some'")
hair = input("Hair of the person (none, yellow, brown, black, white): ")
eyes = input("Eyes of the person (foggy, small green, brown, blue, black): ")
ears = input("Ears of the person (none, small round, small, small cubic): ")
headshape = input("Person shape of head (round, cubic): ")
height = input("Height of the person (small, medium, tall): ")
mouthSize = input("Person size of mouth (none, medium, small, big): ")
languages = input("Language that this person speaks the most (high elfian, universal, force, tatooinean, lunar, universal): ")
skinColor = input("Skin color of the person (blue foggy, white, brown, black): ")

randomPerson = Person(hair, eyes, ears, headshape, height, mouthSize, languages, skinColor)
randomPerson.show_info()

bestComplianceValue = 0
bestComplianceType = None

for personalityType in personsDB.listOfPersonalities:
    complienceDegree = personalityType.compliance_degree(randomPerson)
    if complienceDegree > bestComplianceValue:
        bestComplianceValue = complienceDegree
        bestComplianceType = personalityType
    
print("it is a " + bestComplianceType.show_class())